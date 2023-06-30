from pkg.model import SimpleItemInfo, SimpleLootboxItem
from pkg.utils import random_string

import pkg.client.accelbyte_py_sdk_temp.api.lootbox as platformservice
import pkg.client.accelbyte_py_sdk_temp.api.lootbox.models as platformmodels

from typing import Tuple, List

import pkg.client.accelbyte_py_sdk_temp.api.platform as platform_service
import pkg.client.accelbyte_py_sdk_temp.api.platform.models as platform_models

AB_STORE_NAME = "Python Lootbox Plugin Demo Store"
ALPHA_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

ERR_EMPTY_STORE_ID = "error empty store id, create_store first"
ERR_EMPTY_ITEM_ID = "error empty item id, create_items first"

class PlatformDataUnit:
    def __init__(self, user_info, config, currency_code) -> None:
        self.user_info = user_info
        self.config = config
        self.currency_code = currency_code
        self.store_id = None
    
    def set_platform_service_grpc_target(self):
        if self.config.GRPCServerURL:
            print(f"(Custom Host: {self.config.GRPCServerURL})")

            _, error = platformservice.update_loot_box_plugin_config(
                namespace=self.config.ABNamespace,
                body=platformmodels.LootBoxPluginConfigUpdate.create(
                    extend_type=platformmodels.LootBoxPluginConfigUpdateExtendTypeEnum.CUSTOM,
                    custom_config=platformmodels.BaseCustomConfig.create(
                        connection_type=platformmodels.BaseCustomConfigConnectionTypeEnum.INSECURE,
                        grpc_server_address=self.config.GRPCServerURL
                    )
                )
            )
            return error
            
        if self.config.ExtendAppName:
            print(f"(Extend App: {self.config.ExtendAppName}) ")

            _, error = platformservice.UpdateLootBoxPluginConfig(
                namespace=self.config.ABNamespace,
                body=platformmodels.LootBoxPluginConfigUpdate.create(
                    extend_type=platformmodels.LootBoxPluginConfigUpdateExtendTypeEnum.APP,
                    app_config=platformmodels.AppConfig.create(
                        app_name=self.config.ExtendAppName
                    )
                )
            )
            return error
        
        return None
    
    def creat_store(self, do_publish : bool):         
        result, error = platform_service.create_store(
            namespace=self.config.ABNamespace,
            body=platform_models.StoreCreate.create(
                title=AB_STORE_NAME,
                description="Description for %s" % AB_STORE_NAME,
                default_language="en",
                default_region="US",
                supported_languages=["en"],
                supported_regions=["US"]
            )
        )
        if error:
            return error

        self.store_id = result.store_id
        if do_publish:
            error = self.publish_store_change()
            if error:
                return error

        return error
    
    def publish_store_change(self):
        if not self.store_id:
            return ERR_EMPTY_STORE_ID
        
        _, error = platform_service.publish_all(
            namespace=self.config.ABNamespace,
            store_id=self.store_id
        )
        return error

    def create_category(self, category_path : str, do_publish : bool):
        if not self.store_id:
            return ERR_EMPTY_STORE_ID
        
        _, error = platform_service.create_category(
            namespace=self.config.ABNamespace,
            store_id=self.store_id,
            body=platform_models.CategoryCreate.create(
                category_path=category_path,
                localization_display_names={"en" : category_path}
            )
        )
        if error:
            return error

        if do_publish:
            error = self.publish_store_change()
            if error:
                return error

        return error
    
    def create_currency(self):
        _, error = platform_service.create_currency(
            namespace=self.config.ABNamespace,
            body=platform_models.CurrencyCreate.create(
                currency_code=self.currency_code,
                currency_symbol="USDT1$",
                currency_type=platform_models.CurrencyCreateCurrencyTypeEnum.REAL,
                decimals=2
            ),
        )
        return error
    
    def delete_currency(self):
        return platform_service.delete_currency(
            namespace=self.config.ABNamespace,
            currency_code=self.currency_code
        )

    def unset_platform_service_grpc_target(self):
        _, error = platformservice.delete_loot_box_plugin_config(
            namespace=self.config.ABNamespace
        )
        return error
    
    def delete_store(self):
        if not self.store_id:
            return ERR_EMPTY_STORE_ID
        
        _, error = platform_service.delete_store(
            namespace=self.config.ABNamespace,
            store_id=self.store_id
        )
        return error

    
    def create_items(self, item_count : int, item_diff : str, category_path : str, do_publish : bool):
        if not self.store_id:
            return None, ERR_EMPTY_STORE_ID
        
        items : List[SimpleItemInfo] = list()
        for i in range(item_count):
            item_info = SimpleItemInfo(
                title=f"Item {item_diff} Titled {i+1}",
                sku=f"SKU_{item_diff}_{i+1}"
            )

            newItem, error = platform_service.create_item(
                namespace=self.config.ABNamespace,
                store_id=self.store_id,
                body=platform_models.ItemCreate.create(
                    name=item_info.title,
                    item_type=platform_models.ItemCreateItemTypeEnum.SEASON,
                    category_path=category_path,
                    entitlement_type=platform_models.ItemCreateEntitlementTypeEnum.DURABLE,
                    season_type=platform_models.ItemCreateSeasonTypeEnum.TIER,
                    status=platform_models.ItemCreateStatusEnum.ACTIVE,
                    listable=True,
                    purchasable=True,
                    sku=item_info.sku,
                    localizations={ "en" : platform_models.Localization.create(title=item_info.title) },
                    region_data={ "US" : [platform_models.RegionDataItemDTO.create(
                        currency_code=self.currency_code,
                        currency_namespace=self.config.ABNamespace,
                        currency_type=platform_models.RegionDataItemDTOCurrencyTypeEnum.REAL,
                        price= (i + 1) * 2
                    )]}
                )
            )
            if error:
                return None, "could not create new store item: " + str(error)
            
            item_info.id = newItem.item_id
            items.append(item_info)
                
        if do_publish:
            error = self.publish_store_change()
            if error:
                return None, error

        return items, None

    def create_lootbox_items(self, item_count : int, reward_item_count : int, category_path : str, do_publish : bool):
        if not self.store_id:
            return None, ERR_EMPTY_STORE_ID
        
        lootbox_diff = random_string(ALPHA_CHARS, 6)
        lootbox_items : List[SimpleLootboxItem] = list()
        for i in range(item_count):
            lootbox_item = SimpleLootboxItem(
                title=f"Lootbox Item {lootbox_diff} Titled {i+1}",
                sku=f"SKUCL_{lootbox_diff}_{i+1}",
                diff=lootbox_diff
            )

            lootbox_rewards : List[platform_models.LootBoxReward] = list()
            reward_items : List[SimpleItemInfo] = list()
            for j in range(reward_item_count):
                item_diff = random_string(ALPHA_CHARS, 6)
                items, error = self.create_items(item_count=1, category_path=category_path, item_diff=item_diff, do_publish=do_publish)
                if error:
                    return None, error
                
                reward_box_items : platform_models.BoxItem = list()
                for item_info in items:
                    if not item_info.id:
                        return None, ERR_EMPTY_ITEM_ID
                    reward_box_items.append(platform_models.BoxItem.create(
                        count=1,
                        item_id=item_info.id,
                        item_sku=item_info.sku
                    ))
                    reward_items.append(item_info)

                lootbox_reward = platform_models.LootBoxReward.create(
                    name=f"Reward-{item_diff}",
                    odds=0.1,
                    weight=10,
                    type_=platform_models.LootBoxRewardTypeEnum.REWARD,
                    loot_box_items=reward_box_items
                )
                lootbox_rewards.append(lootbox_reward)

            lootbox_item.reward_items = reward_items
            new_item, error = platform_service.create_item(
                namespace=self.config.ABNamespace,
                store_id=self.store_id,
                body=platform_models.ItemCreate.create(
                    name=lootbox_item.title,
                    item_type=platform_models.ItemCreateItemTypeEnum.LOOTBOX,
                    category_path=category_path,
                    entitlement_type=platform_models.ItemCreateEntitlementTypeEnum.CONSUMABLE,
                    season_type=platform_models.ItemCreateSeasonTypeEnum.TIER,
                    status=platform_models.ItemCreateStatusEnum.ACTIVE,
                    use_count=100,
                    listable=True,
                    purchasable=True,
                    sku=lootbox_item.sku,
                    loot_box_config=platform_models.LootBoxConfig.create(
                        reward_count= reward_item_count,
                        rewards=lootbox_rewards,
                        roll_function=platform_models.LootBoxConfigRollFunctionEnum.CUSTOM
                    ),
                    localizations={ "en" : platform_models.Localization.create(title=lootbox_item.title) },
                    region_data={ "US" : [platform_models.RegionDataItemDTO.create(
                        currency_code=self.currency_code,
                        currency_namespace=self.config.ABNamespace,
                        currency_type=platform_models.RegionDataItemDTOCurrencyTypeEnum.REAL,
                        price= (i + 1) * 2
                    )]}
                )
            )
            if error:
                return None, error
            elif new_item is None:
                return None, "could not create new lootbox item"
            
            lootbox_item.id = new_item.item_id
            lootbox_items.append(lootbox_item)

        if do_publish:
            error = self.publish_store_change()
            if error:
                return None, error
        
        return lootbox_items, None
        
    def grant_entitlement(self, user_id : str, item_id : str, count : int):
        if not self.store_id:
            return "", ERR_EMPTY_STORE_ID
        
        entitlement_info, error = platform_service.grant_user_entitlement(
            namespace=self.config.ABNamespace,
            user_id=user_id,
            body=[platform_models.EntitlementGrant.create(
                item_id=item_id,
                quantity=count,
                source=platform_models.EntitlementGrantSourceEnum.GIFT,
                item_namespace=self.config.ABNamespace
            )]
        )
        if error:
            return "", error
        elif len(entitlement_info) <= 0:
            return "", "could not grant item to user"
        
        return entitlement_info[0].id_, None
            
    def consume_item_entitlement(self, user_id : str, entitlement_id : str, count : int):      

        result, error = platform_service.consume_user_entitlement(
            namespace=self.config.ABNamespace,
            entitlement_id=entitlement_id,
            user_id=user_id,
            body=platform_models.EntitlementDecrement.create(
                use_count=count,
                request_id=random_string(ALPHA_CHARS, 8)
            )
        )
        if error:
            return None, error

        lootbox_item = SimpleLootboxItem(id=result.id_)
        items : List[SimpleItemInfo] = list()
        for it in result.rewards:
            items.append(SimpleItemInfo(
                id=it.item_id,
                sku=it.item_sku
            ))
        lootbox_item.reward_items = items

        return lootbox_item, None