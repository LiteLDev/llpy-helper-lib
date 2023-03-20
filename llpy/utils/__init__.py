from typing import TYPE_CHECKING

from llpy.classes.mc import mc

if TYPE_CHECKING:
    from .types import T_EventCallback, T_EventName


def listen(event: T_EventName):
    """
    监听事件函数装饰器

    Args:
        event: 要监听的事件名称
    """

    def wrapper(func: T_EventCallback):
        mc.listen(event, func)
        return func

    return wrapper
