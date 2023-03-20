from typing import TYPE_CHECKING

from . import mc

if TYPE_CHECKING:
    from .mc import _T_Event, _T_EventCallback


def listen(event: "_T_Event"):
    """
    监听事件函数装饰器

    Args:
        event: 要监听的事件名称
    """

    def wrapper(func: _T_EventCallback):
        mc.listen(event, func)
        return func

    return wrapper
