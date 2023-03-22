from typing import TypedDict


class T_HttpGetResp(TypedDict):
    """`network.httpGetSync()` 返回的响应结果"""

    status: int
    """返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`"""
    data: str
    """返回的具体数据"""
