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
            userId = "b52a2364226d436285c1b8786bc9cbd1",
            namespace = "accelbyte",
            quantity = 10,
            itemInfo = LootBoxItemInfo(
                itemId = "8a0b8bda28c845f6938cc57540af452e",
                itemSku = "SKU3170",
                rewardCount = 2,
                lootBoxRewards = [LootBoxItemInfo.LootBoxRewardObject(
                    name = "Foods",
                    type = "REWARD",
                    weight = 5,
                    odds = 0,
                    items = [BoxItemObject(
                        itemId = "8b6016d243264c0f90031600313b8a37",
                        itemSku = "SKU4650",
                        count = 5
                    )]
                )]
            ),
        )

        response = await self.service.RollLootBoxRewards(request, None)

        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, RollLootBoxRewardsResponse)

