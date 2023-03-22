from typing import Literal, TypedDict

from typing_extensions import deprecated

from llpy import LLSE_Item


@deprecated("请使用 `LLSE_Player.getInventory()`")
class T_PlayerInventory(TypedDict):
    """`LLSE_Player.getAllItems()` 返回的物品栏信息"""

    hand: LLSE_Item
    offHand: LLSE_Item
    inventory: list[LLSE_Item]
    armor: list[LLSE_Item]
    endChest: list[LLSE_Item]


T_PermLevel = Literal[0, 1, 2, 3, 4]
"""玩家的操作权限等级。`0` 为普通成员，`1` 为 OP，`4` 为控制台"""
T_GameMode = Literal[0, 1, 2, 3]
"""玩家的游戏模式。0-3 依次为 生存、创造、冒险、旁观"""
