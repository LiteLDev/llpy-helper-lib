from typing import Literal, TypedDict


class T_RunCmdExRet(TypedDict):
    """`mc.runCmdEx()` 的返回值"""

    success: bool
    """是否执行成功"""
    output: str
    """BDS 执行命令后的输出结果"""


T_BroadcastType_RAW = Literal[0]
"""普通消息"""
T_BroadcastType_CHAT = Literal[1]
"""聊天消息"""
T_BroadcastType_TRANSLATION = Literal[2]
T_BroadcastType_POPUP = Literal[3]
T_BroadcastType_JUKEBOX_POPUP = Literal[4]
T_BroadcastType_TIP = Literal[5]
"""物品栏上方的消息"""
T_BroadcastType_SYSTEM = Literal[6]
T_BroadcastType_WHISPER = Literal[7]
T_BroadcastType_ANNOUNCEMENT = Literal[8]
T_BroadcastType_JSON_WHISPER = Literal[9]
"""JSON 格式消息"""
T_BroadcastType_JSON = Literal[10]
T_BroadcastType = (
    T_BroadcastType_RAW
    | T_BroadcastType_CHAT
    | T_BroadcastType_TRANSLATION
    | T_BroadcastType_POPUP
    | T_BroadcastType_JUKEBOX_POPUP
    | T_BroadcastType_TIP
    | T_BroadcastType_SYSTEM
    | T_BroadcastType_WHISPER
    | T_BroadcastType_ANNOUNCEMENT
    | T_BroadcastType_JSON_WHISPER
    | T_BroadcastType_JSON
)
"""`mc.broadcast()` 的文本消息类型参数"""
