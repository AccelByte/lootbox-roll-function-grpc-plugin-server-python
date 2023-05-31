# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import asyncio
import logging

from logging import Logger
from typing import Optional
from enum import IntFlag
from argparse import ArgumentParser

from environs import Env

from app.proto.lootbox_pb2_grpc import add_LootBoxServicer_to_server

from accelbyte_grpc_plugin.opts.loki import LokiOpt
from accelbyte_grpc_plugin.opts.zipkin import ZipkinOpt
from accelbyte_grpc_plugin import App, AppGRPCInterceptorOpt, AppGRPCServiceOpt
from accelbyte_grpc_plugin.interceptors.logging import DebugLoggingServerInterceptor
from accelbyte_grpc_plugin.interceptors.metrics import MetricsServerInterceptor
from accelbyte_grpc_plugin.interceptors.authorization import AuthorizationServerInterceptor
from app.services.lootbox_service import AsyncLootBoxService

DEFAULT_APP_PORT: int = 6565

class PermissionAction(IntFlag):
    CREATE = 0b0001
    READ = 0b0010
    UPDATE = 0b0100
    DELETE = 0b1000

async def main(port:int, logger: Optional[Logger] = None, **kwargs) -> None:
    
    # setup logger
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    # setup env reading config
    env = Env(
        eager=kwargs.get("env_eager", True),
        expand_vars=kwargs.get("env_expand_vars", False),
    )
    env.read_env(
        path=kwargs.get("env_path", None),
        recurse=kwargs.get("env_recurse", True),
        verbose=kwargs.get("env_verbose", False),
        override=kwargs.get("env_override", False),
    )

    with env.prefixed("AB_"):
        base_url = env("BASE_URL", "https://demo.accelbyte.io")
        client_id = env("CLIENT_ID", None)
        client_secret = env("CLIENT_SECRET", None)
        namespace = env("NAMESPACE", "accelbyte")

    opts = []
    with env.prefixed(prefix="ENABLE_"):
        if env.bool("LOKI", True):
            opts.append(LokiOpt())
        if env.bool("ZIPKIN", True):
            opts.append(ZipkinOpt())
    
    # login if specified
    with env.prefixed(prefix="PLUGIN_GRPC_SERVER_AUTH_"):
        if env.bool("ENABLED", False):
            from accelbyte_py_sdk import AccelByteSDK
            from accelbyte_py_sdk.core import MyConfigRepository, InMemoryTokenRepository
            from accelbyte_py_sdk.token_validation.caching import CachingTokenValidator

            resource = env("RESOURCE", "NAMESPACE:{namespace}:PLRGRPCSERVICE")
            action = env.int("ACTION", int(PermissionAction.READ))

            config = MyConfigRepository(
                base_url, client_id, client_secret, namespace=namespace
            )
            sdk = AccelByteSDK()
            sdk.initialize(options={"config": config, "token": InMemoryTokenRepository()})
            token_validator = CachingTokenValidator(sdk)
            auth_server_interceptor = AuthorizationServerInterceptor(
                resource=resource,
                action=action,
                namespace=namespace,
                token_validator=token_validator,
            )
            opts.append(AppGRPCInterceptorOpt(auth_server_interceptor))
    
    if env.bool("PLUGIN_GRPC_SERVER_LOGGING_ENABLED", False):
        opts.append(AppGRPCInterceptorOpt(DebugLoggingServerInterceptor(logger)))

    if env.bool("PLUGIN_GRPC_SERVER_METRICS_ENABLED", True):
        opts.append(AppGRPCInterceptorOpt(MetricsServerInterceptor()))

    opts.append(
        AppGRPCServiceOpt(
            AsyncLootBoxService(
                logger=logger
            ),
            AsyncLootBoxService.full_name,
            add_LootBoxServicer_to_server,
        )
    )
    
    logger.info("setup completed, running interceptors")

    await App(port, env, opts=opts).run()
            
def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        "-p",
        "--port",
        default=DEFAULT_APP_PORT,
        type=int,
        required=False,
        help="[P]ort",
    )

    result = vars(parser.parse_args())

    return result


if __name__ == "__main__":
    asyncio.run(main(**parse_args()))