# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import random

from logging import Logger, getLogger
from typing import List, Optional

from app.proto.lootbox_pb2 import (
    RollLootBoxRewardsRequest,
    RollLootBoxRewardsResponse,
    RewardObject,
    LootBoxItemInfo,
    BoxItemObject,
    DESCRIPTOR,
)
from app.proto.lootbox_pb2_grpc import LootBoxServicer

class AsyncLootBoxService(LootBoxServicer):
    
    def __init__(self, logger: Optional[Logger]) -> None:
        self.logger = (
            logger if logger is not None else getLogger(self.__class__.__name__)
        )
            
    async def RollLootBoxRewards(self, request: RollLootBoxRewardsRequest, context):
        self.logger.info("Received rollLootBoxRewards request")

        final_items: List[RewardObject] = []
        rewards: List[LootBoxItemInfo.LootBoxRewardObject] = request.itemInfo.lootBoxRewards
        reward_weight_sum: int = 0

        reward_weight_sum = sum(reward.weight for reward in rewards)

        for i in range(request.quantity):
            for sel_idx in range(len(rewards)):
                r = random.random() * reward_weight_sum
                r -= rewards[sel_idx].weight
                if r <= 0.0:
                    break
            
            
            sel_reward: LootBoxItemInfo.LootBoxRewardObject = rewards[sel_idx]
            item_count: int = len(sel_reward.items)

            sel_item_idx: int = random.randint(0, item_count-1)
            sel_item: BoxItemObject = sel_reward.items[sel_item_idx]

            reward_item: RewardObject = RewardObject(
                itemId=sel_item.itemId,
                itemSku=sel_item.itemSku,
                count=sel_item.count,
            )
            final_items.append(reward_item)
        
        response: RollLootBoxRewardsResponse = RollLootBoxRewardsResponse(
            rewards=final_items
        )

        return response