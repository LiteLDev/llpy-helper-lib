from llpy.utils.types import T_EventCallback, T_EventName

class mc:
    """MC API"""

    @staticmethod
    def listen(event: T_EventName, callback: T_EventCallback) -> bool:
        """
        注册监听器

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数
                当指定的事件发生时，BDS会调用你给出的监听函数，并传入相应的参数

        Returns:
            是否成功监听事件
        """
