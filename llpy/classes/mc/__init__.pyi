from typing import Any, Callable, Literal, NoReturn, overload

from llpy import ParticleSpawner

class mc:
    """MC API"""

    def __init__(self) -> NoReturn: ...
    @overload
    @staticmethod
    def listen(
        event: Literal["onServerStarted"],
        callback: Callable[[], Any],
    ) -> bool:
        """
        注册监听器

        服务器启动完毕 监听

        拦截事件：不可以拦截

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onConsoleCmd"],
        callback: Callable[[str], Any],
    ) -> bool:
        """
        注册监听器

        服务端执行后台命令 监听

        拦截事件：函数返回 `False`

        Callback Args:
            cmd (str): 执行的后台命令

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @staticmethod
    def newParticleSpawner(
        display_radius: int,
        high_detail: bool,
        double_side: bool,
    ) -> ParticleSpawner:
        """
        生成一个粒子生成器对象

        Args:
            display_radius: 粒子显示半径
            high_detail: 需要高细节线条
            double_side: 需要双面粒子

        Returns:
            一个粒子生成器对象
        """

# TODO
