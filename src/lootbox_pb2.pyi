from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoxItemObject(_message.Message):
    __slots__ = ["count", "itemId", "itemSku"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMSKU_FIELD_NUMBER: _ClassVar[int]
    count: int
    itemId: str
    itemSku: str
    def __init__(self, itemId: _Optional[str] = ..., itemSku: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class LootBoxItemInfo(_message.Message):
    __slots__ = ["itemId", "itemSku", "lootBoxRewards", "rewardCount"]
    class LootBoxRewardObject(_message.Message):
        __slots__ = ["items", "name", "odds", "type", "weight"]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ODDS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[BoxItemObject]
        name: str
        odds: float
        type: str
        weight: int
        def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., items: _Optional[_Iterable[_Union[BoxItemObject, _Mapping]]] = ..., weight: _Optional[int] = ..., odds: _Optional[float] = ...) -> None: ...
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMSKU_FIELD_NUMBER: _ClassVar[int]
    LOOTBOXREWARDS_FIELD_NUMBER: _ClassVar[int]
    REWARDCOUNT_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    itemSku: str
    lootBoxRewards: _containers.RepeatedCompositeFieldContainer[LootBoxItemInfo.LootBoxRewardObject]
    rewardCount: int
    def __init__(self, itemId: _Optional[str] = ..., itemSku: _Optional[str] = ..., rewardCount: _Optional[int] = ..., lootBoxRewards: _Optional[_Iterable[_Union[LootBoxItemInfo.LootBoxRewardObject, _Mapping]]] = ...) -> None: ...

class RewardObject(_message.Message):
    __slots__ = ["count", "itemId", "itemSku"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMSKU_FIELD_NUMBER: _ClassVar[int]
    count: int
    itemId: str
    itemSku: str
    def __init__(self, itemId: _Optional[str] = ..., itemSku: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class RollLootBoxRewardsRequest(_message.Message):
    __slots__ = ["itemInfo", "namespace", "quantity", "userId"]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    itemInfo: LootBoxItemInfo
    namespace: str
    quantity: int
    userId: str
    def __init__(self, userId: _Optional[str] = ..., namespace: _Optional[str] = ..., quantity: _Optional[int] = ..., itemInfo: _Optional[_Union[LootBoxItemInfo, _Mapping]] = ...) -> None: ...

class RollLootBoxRewardsResponse(_message.Message):
    __slots__ = ["rewards"]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    rewards: _containers.RepeatedCompositeFieldContainer[RewardObject]
    def __init__(self, rewards: _Optional[_Iterable[_Union[RewardObject, _Mapping]]] = ...) -> None: ...
