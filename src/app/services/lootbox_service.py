# Copyright (c) 2025 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
import random
from logging import Logger
from typing import List, Optional

from google.protobuf.json_format import MessageToDict

from accelbyte_py_sdk import AccelByteSDK

from ..proto.lootbox_pb2 import (
    RollLootBoxRewardsRequest,
    RollLootBoxRewardsResponse,
    RewardObject,
    LootBoxItemInfo,
    BoxItemObject,
    DESCRIPTOR,
)
from ..proto.lootbox_pb2_grpc import LootBoxServicer


class AsyncLootBoxService(LootBoxServicer):
    full_name: str = DESCRIPTOR.services_by_name["LootBox"].full_name

    def __init__(self, sdk: Optional[AccelByteSDK] = None, logger: Optional[Logger] = None) -> None:
        self.sdk = sdk
        self.logger = logger
            
    async def RollLootBoxRewards(self, request: RollLootBoxRewardsRequest, context):
        self.log_payload(f'{self.RollLootBoxRewards.__name__} request: %s', request)

        rewards: List[LootBoxItemInfo.LootBoxRewardObject] = request.itemInfo.lootBoxRewards
        reward_weight_sum: int = 0
        reward_weight_sum = sum(reward.weight for reward in rewards)

        final_items: List[RewardObject] = []
        for _ in range(request.quantity):
            r = random.random() * reward_weight_sum

            selected_index = 0
            for i in range(len(rewards)):
                selected_index = i
                r -= rewards[selected_index].weight
                if r <= 0.0:
                    break

            selected_reward: LootBoxItemInfo.LootBoxRewardObject = rewards[selected_index]
            item_count: int = len(selected_reward.items)

            selected_item_index: int = random.randint(0, item_count-1)
            selected_item: BoxItemObject = selected_reward.items[selected_item_index]

            reward_item: RewardObject = RewardObject(
                itemId=selected_item.itemId,
                itemSku=selected_item.itemSku,
                count=selected_item.count,
            )
            final_items.append(reward_item)

        response: RollLootBoxRewardsResponse = RollLootBoxRewardsResponse(
            rewards=final_items
        )
        self.log_payload(f'{self.RollLootBoxRewards.__name__} response: %s', response)

        return response

    # noinspection PyShadowingBuiltins
    def log_payload(self, format : str, payload):
        if not self.logger:
            return
        payload_dict = MessageToDict(payload, preserving_proto_field_name=True)
        payload_json = json.dumps(payload_dict)
        self.logger.info(format % payload_json)
