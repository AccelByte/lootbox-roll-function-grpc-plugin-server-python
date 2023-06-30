# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
# 
# Code generated. DO NOT EDIT!

# template file: ags_py_codegen

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import HeaderStr
from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import run_request_async
from ....core import deprecated
from ....core import same_doc_as

from ..models import DebitRequest
from ..models import DetailedWalletTransactionPagingSlicedResult
from ..models import ErrorEntity
from ..models import ValidationErrorEntity
from ..models import WalletInfo
from ..models import WalletPagingSlicedResult

from ..operations.wallet_deprecated import CheckWallet
from ..operations.wallet_deprecated import CheckWalletOriginEnum
from ..operations.wallet_deprecated import DebitUserWallet
from ..operations.wallet_deprecated import DisableUserWallet
from ..operations.wallet_deprecated import EnableUserWallet
from ..operations.wallet_deprecated import GetUserWallet
from ..operations.wallet_deprecated import GetWallet
from ..operations.wallet_deprecated import ListUserWalletTransactions
from ..operations.wallet_deprecated import QueryWallets
from ..operations.wallet_deprecated import QueryWalletsOriginEnum
from ..models import WalletInfoStatusEnum


@deprecated
@same_doc_as(CheckWallet)
def check_wallet(currency_code: str, origin: Union[str, CheckWalletOriginEnum], user_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Check wallet by balance origin and currency code (checkWallet)

    [SERVICE COMMUNICATION ONLY] Check wallet by balance origin and currency code whether it's inactive.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=2 (READ)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{currencyCode}/check

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        currency_code: (currencyCode) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        origin: (origin) REQUIRED Union[str, OriginEnum] in query

    Responses:
        204: No Content - (check successfully)

        400: Bad Request - ErrorEntity (35123: Wallet [{walletId}] is inactive)

        409: Conflict - ErrorEntity (20006: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (20002: validation error)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CheckWallet.create(
        currency_code=currency_code,
        origin=origin,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(CheckWallet)
async def check_wallet_async(currency_code: str, origin: Union[str, CheckWalletOriginEnum], user_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Check wallet by balance origin and currency code (checkWallet)

    [SERVICE COMMUNICATION ONLY] Check wallet by balance origin and currency code whether it's inactive.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=2 (READ)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{currencyCode}/check

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        currency_code: (currencyCode) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        origin: (origin) REQUIRED Union[str, OriginEnum] in query

    Responses:
        204: No Content - (check successfully)

        400: Bad Request - ErrorEntity (35123: Wallet [{walletId}] is inactive)

        409: Conflict - ErrorEntity (20006: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (20002: validation error)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CheckWallet.create(
        currency_code=currency_code,
        origin=origin,
        user_id=user_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(DebitUserWallet)
def debit_user_wallet(user_id: str, wallet_id: str, body: Optional[DebitRequest] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Debit a user wallet (debitUserWallet)

    Debit a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=4 (UPDATE)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/debit

        method: PUT

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        body: (body) OPTIONAL DebitRequest in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        200: OK - WalletInfo (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)

        400: Bad Request - ErrorEntity (35123: Wallet [{walletId}] is inactive | 35124: Wallet [{currencyCode}] has insufficient balance)

        409: Conflict - ErrorEntity (20006: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (20002: validation error)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DebitUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(DebitUserWallet)
async def debit_user_wallet_async(user_id: str, wallet_id: str, body: Optional[DebitRequest] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Debit a user wallet (debitUserWallet)

    Debit a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=4 (UPDATE)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/debit

        method: PUT

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        body: (body) OPTIONAL DebitRequest in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        200: OK - WalletInfo (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)

        400: Bad Request - ErrorEntity (35123: Wallet [{walletId}] is inactive | 35124: Wallet [{currencyCode}] has insufficient balance)

        409: Conflict - ErrorEntity (20006: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (20002: validation error)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DebitUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        body=body,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(DisableUserWallet)
def disable_user_wallet(user_id: str, wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Disable a user wallet (disableUserWallet)

    disable a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=4 (UPDATE)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/disable

        method: PUT

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        204: No Content - (Successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)

        409: Conflict - ErrorEntity (20006: optimistic lock)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DisableUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(DisableUserWallet)
async def disable_user_wallet_async(user_id: str, wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Disable a user wallet (disableUserWallet)

    disable a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=4 (UPDATE)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/disable

        method: PUT

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        204: No Content - (Successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)

        409: Conflict - ErrorEntity (20006: optimistic lock)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DisableUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(EnableUserWallet)
def enable_user_wallet(user_id: str, wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Enable a user wallet (enableUserWallet)

    enable a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=4 (UPDATE)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/enable

        method: PUT

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        204: No Content - (Successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)

        409: Conflict - ErrorEntity (20006: optimistic lock)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = EnableUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(EnableUserWallet)
async def enable_user_wallet_async(user_id: str, wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Enable a user wallet (enableUserWallet)

    enable a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=4 (UPDATE)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/enable

        method: PUT

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        204: No Content - (Successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)

        409: Conflict - ErrorEntity (20006: optimistic lock)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = EnableUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(GetUserWallet)
def get_user_wallet(user_id: str, wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Get a user wallet (getUserWallet)

    get a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=2 (READ)
      *  Returns : wallet info

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        200: OK - WalletInfo (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(GetUserWallet)
async def get_user_wallet_async(user_id: str, wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Get a user wallet (getUserWallet)

    get a user wallet.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=2 (READ)
      *  Returns : wallet info

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        200: OK - WalletInfo (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserWallet.create(
        user_id=user_id,
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(GetWallet)
def get_wallet(wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Get a wallet by wallet id (getWallet)

    get a wallet by wallet id.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:WALLET", action=2 (READ)
      *  Returns : wallet info

    Properties:
        url: /platform/admin/namespaces/{namespace}/wallets/{walletId}

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        200: OK - WalletInfo (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetWallet.create(
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(GetWallet)
async def get_wallet_async(wallet_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Get a wallet by wallet id (getWallet)

    get a wallet by wallet id.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:WALLET", action=2 (READ)
      *  Returns : wallet info

    Properties:
        url: /platform/admin/namespaces/{namespace}/wallets/{walletId}

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

    Responses:
        200: OK - WalletInfo (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetWallet.create(
        wallet_id=wallet_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(ListUserWalletTransactions)
def list_user_wallet_transactions(user_id: str, wallet_id: str, limit: Optional[int] = None, offset: Optional[int] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """List user wallet transactions (listUserWalletTransactions)

    List user wallet transactions ordered by create time desc.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=2 (READ)
      *  Returns : wallet transaction info

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/transactions

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

        limit: (limit) OPTIONAL int in query

        offset: (offset) OPTIONAL int in query

    Responses:
        200: OK - DetailedWalletTransactionPagingSlicedResult (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListUserWalletTransactions.create(
        user_id=user_id,
        wallet_id=wallet_id,
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(ListUserWalletTransactions)
async def list_user_wallet_transactions_async(user_id: str, wallet_id: str, limit: Optional[int] = None, offset: Optional[int] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """List user wallet transactions (listUserWalletTransactions)

    List user wallet transactions ordered by create time desc.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:WALLET", action=2 (READ)
      *  Returns : wallet transaction info

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{walletId}/transactions

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        wallet_id: (walletId) REQUIRED str in path

        limit: (limit) OPTIONAL int in query

        offset: (offset) OPTIONAL int in query

    Responses:
        200: OK - DetailedWalletTransactionPagingSlicedResult (successful operation)

        404: Not Found - ErrorEntity (35141: Wallet [{walletId}] does not exist)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListUserWalletTransactions.create(
        user_id=user_id,
        wallet_id=wallet_id,
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(QueryWallets)
def query_wallets(currency_code: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, origin: Optional[Union[str, QueryWalletsOriginEnum]] = None, user_id: Optional[str] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Query wallets (queryWallets)

    Query wallets.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:WALLET", action=2 (READ)
      *  Returns : paginated wallets info

    Properties:
        url: /platform/admin/namespaces/{namespace}/wallets

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        currency_code: (currencyCode) OPTIONAL str in query

        limit: (limit) OPTIONAL int in query

        offset: (offset) OPTIONAL int in query

        origin: (origin) OPTIONAL Union[str, OriginEnum] in query

        user_id: (userId) OPTIONAL str in query

    Responses:
        200: OK - WalletPagingSlicedResult (successful operation)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QueryWallets.create(
        currency_code=currency_code,
        limit=limit,
        offset=offset,
        origin=origin,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@deprecated
@same_doc_as(QueryWallets)
async def query_wallets_async(currency_code: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, origin: Optional[Union[str, QueryWalletsOriginEnum]] = None, user_id: Optional[str] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    """Query wallets (queryWallets)

    Query wallets.
    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:WALLET", action=2 (READ)
      *  Returns : paginated wallets info

    Properties:
        url: /platform/admin/namespaces/{namespace}/wallets

        method: GET

        tags: ["Wallet(Deprecated)"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        currency_code: (currencyCode) OPTIONAL str in query

        limit: (limit) OPTIONAL int in query

        offset: (offset) OPTIONAL int in query

        origin: (origin) OPTIONAL Union[str, OriginEnum] in query

        user_id: (userId) OPTIONAL str in query

    Responses:
        200: OK - WalletPagingSlicedResult (successful operation)
    """
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QueryWallets.create(
        currency_code=currency_code,
        limit=limit,
        offset=offset,
        origin=origin,
        user_id=user_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers, **kwargs)
