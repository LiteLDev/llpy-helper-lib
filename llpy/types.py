from typing import Any, Literal, TypedDict

T_ColorName = Literal[
    "blue",
    "sky_blue",
    "green",
    "red",
    "cyan",
    "yellow",
    "pink",
    "dk_blue",
    "dk_green",
    "dk_red",
    "bt_blue",
    "dk_yellow",
    "purple",
    "white",
    "grey",
]
"""`colorLog` 可传入的颜色名称"""

T_LogLevel = Literal[0, 1, 2, 3, 4, 5]
"""
日志输出等级

0. `Slient` - 不输出任何日志

1. `Fatal` - 仅输出 严重错误信息

2. `Error` - 输出 严重错误、错误信息

3. `Warn` - 输出 严重错误、错误、警告信息

4. `Info` - 输出 严重错误、错误、警告、提示信息

5. `Debug` - 输出 严重错误、错误、警告、提示 和 调试信息
"""

T_ToIniType = int | float | str | bool

T_ToJsonBase = int | float | str | bool
T_ToJsonList = list["T_ToJsonType"]
T_ToJsonDict = dict[str, "T_ToJsonType"]
T_ToJsonType = T_ToJsonBase | T_ToJsonList | T_ToJsonDict


class T_TimeObj(TypedDict):
    """`system.getTimeObj()` 获取到的时间对象"""

    Y: int
    """年份数值（4位）"""
    M: int
    """月份数值"""
    D: int
    """天数数值"""
    h: int
    """小时数值（24小时制）"""
    m: int
    """分钟数值"""
    s: int
    """秒数值"""
    ms: int
    """毫秒数值"""


class T_PlayerInfo(TypedDict):
    """
    `data.getAllPlayerInfo()` 获取到的玩家信息

    提示：XUID 数据库中储存的玩家名为玩家对象对应的 `realName` 字段
    """

    name: str
    """玩家名"""
    xuid: str
    """玩家XUID"""
    uuid: str
    """玩家UUID"""


class T_PluginInfo(TypedDict):
    """`ll.getPluginInfo()` 或 `ll.getAllPluginInfo()` 返回的插件信息"""

    name: str
    """插件名称"""
    desc: str
    """插件描述"""
    version: list[int]
    """插件版本（数组形式）"""
    versionStr: str
    """插件版本"""
    filePath: str
    """插件路径"""
    others: dict[str, str]
    """其他信息"""
