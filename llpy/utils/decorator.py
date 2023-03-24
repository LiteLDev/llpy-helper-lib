from typing import Any, Callable

from llpy import LLSE_Command, mc
from llpy.types import T_CommandCallback


def listener(event: str):
    """
    监听事件函数装饰器

    Args:
        event: 要监听的事件名称
    """

    def wrapper(func: Callable[..., Any]):
        mc.listen(event, func)  # pyright: ignore[reportGeneralTypeIssues]
        return func

    return wrapper


def command_callback(cmd: LLSE_Command):
    """
    指令回调装饰器

    Args:
        cmd: 要设置回调的指令
    """

    def wrapper(func: T_CommandCallback):
        cmd.setCallback(func)
        return func

    return wrapper
