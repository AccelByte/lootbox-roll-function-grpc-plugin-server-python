# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
import asyncio
from typing import List
from unittest import IsolatedAsyncioTestCase
import uuid

from app.proto.lootbox_pb2 import (
    RollLootBoxRewardsRequest, 
    RollLootBoxRewardsResponse, 
    LootBoxItemInfo, 
    BoxItemObject,
)
from app.proto.lootbox_pb2_grpc import (
    LootBoxStub,
    add_LootBoxServicer_to_server,
)
from app.services.lootbox_service import AsyncLootBoxService

from accelbyte_grpc_plugin_tests import create_server

class AsyncLootBoxServiceTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.service = AsyncLootBoxService(None)

    async def test_filter_bulk_filters_profanities(self):
       
        request = RollLootBoxRewardsRequest(
            userId = "",
            namespace = "accelbyte",
            quantity = 10,
            itemInfo = LootBoxItemInfo(
                itemId = "",
                itemSku = "SKU3170",
                rewardCount = 2,
                lootBoxRewards = [LootBoxItemInfo.LootBoxRewardObject(
                    name = "Foods",
                    type = "REWARD",
                    weight = 5,
                    odds = 0,
                    items = [BoxItemObject(
                        itemId = "",
                        itemSku = "",
                        count = 5
                    )]
                )]
            ),
        )

        response = await self.service.RollLootBoxRewards(request, None)

        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, RollLootBoxRewardsResponse)

