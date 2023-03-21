from typing import Literal, TypedDict

from . import (
    NbtByte,
    NbtByteArray,
    NbtCompound,
    NbtDouble,
    NbtEnd,
    NbtFloat,
    NbtInt,
    NbtList,
    NbtLong,
    NbtShort,
    NbtString,
)

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


T_VersionStatusDev = Literal[0]
T_VersionStatusBeta = Literal[1]
T_VersionStatusRelease = Literal[2]
T_VersionStatus = T_VersionStatusDev | T_VersionStatusBeta | T_VersionStatusRelease


T_WSClientStatusOpen = Literal[0]
T_WSClientStatusClosing = Literal[1]
T_WSClientStatusClosed = Literal[2]
T_WSClientStatus = (
    T_WSClientStatusOpen | T_WSClientStatusClosing | T_WSClientStatusClosed
)


T_NbtTypeEnd = Literal[0]
T_NbtTypeByte = Literal[1]
T_NbtTypeShort = Literal[2]
T_NbtTypeInt = Literal[3]
T_NbtTypeLong = Literal[4]
T_NbtTypeFloat = Literal[5]
T_NbtTypeDouble = Literal[6]
T_NbtTypeByteArray = Literal[7]
T_NbtTypeString = Literal[8]
T_NbtTypeList = Literal[9]
T_NbtTypeCompound = Literal[10]
T_NbtType = (
    T_NbtTypeEnd
    | T_NbtTypeByte
    | T_NbtTypeShort
    | T_NbtTypeInt
    | T_NbtTypeLong
    | T_NbtTypeFloat
    | T_NbtTypeDouble
    | T_NbtTypeByteArray
    | T_NbtTypeString
    | T_NbtTypeList
    | T_NbtTypeCompound
)

T_NbtBaseClass = (
    NbtEnd
    | NbtByte
    | NbtShort
    | NbtInt
    | NbtLong
    | NbtFloat
    | NbtDouble
    | NbtByteArray
    | NbtString
)
T_NbtClass = T_NbtBaseClass | NbtCompound | NbtList

T_ToNbtBase = int | float | str | bytearray | None
T_ToNbtList = list["T_ToNbtType"]
T_ToNbtDict = dict[str, "T_ToNbtType"]
T_ToNbtType = T_ToNbtBase | T_ToNbtList | T_ToNbtDict


T_ToIniType = int | float | str | bool

T_ToJsonBase = int | float | str | bool | None
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


T_MoneyHistory = TypedDict(
    "T_MoneyHistory",
    {
        "from": str,  # 此项交易的发起者玩家 XUID
        "to": str,  # 此项交易的接收者玩家 XUID
        "money": int,  # 此项交易的金额
        "time": str,  # 此项交易发生时的时间字符串，格式为：YYYY-mm-dd hh:mm:ss
        "note": str,  # 此交易的附加说明信息
    },
)
"""`money.getHistory()` 返回的历史账单信息"""


class T_HttpGetResp(TypedDict):
    """`network.httpGetSync()` 返回的响应结果"""

    status: int
    """返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`"""
    data: str
    """返回的具体数据"""
