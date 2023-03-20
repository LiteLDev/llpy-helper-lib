from typing import Callable, Literal, NoReturn, overload

class mc:
    """MC API"""

    def __init__(self) -> NoReturn: ...
    @overload
    @staticmethod
    def listen(
        event: Literal["onServerStarted"],
        callback: Callable[[], bool | None],
    ) -> bool:
        """服务器启动完毕监听"""
    @overload
    @staticmethod
    def listen(
        event: Literal["onConsoleCmd"],
        callback: Callable[[str], bool | None],
    ) -> bool:
        """服务端执行后台命令监听"""
    @staticmethod
    def listen(event: str, callback: Callable[..., bool | None]) -> bool:
        """
        注册监听器

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数
                当指定的事件发生时，BDS会调用你给出的监听函数，并传入相应的参数

        Returns:
            是否成功监听事件
        """
