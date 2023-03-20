from typing import Any, Literal, Tuple

from .player import Player

_T_LogLevel = Literal[0, 1, 2, 3, 4, 5]
"""
日志输出等级

0. `Slient` - 不输出任何日志

1. `Fatal` - 仅输出 严重错误信息

2. `Error` - 输出 严重错误、错误信息

3. `Warn` - 输出 严重错误、错误、警告信息

4. `Info` - 输出 严重错误、错误、警告、提示信息

5. `Debug` - 输出 严重错误、错误、警告、提示 和 调试信息
"""

class logger:
    """通用日志 API"""

    @staticmethod
    def setConsole(is_open: bool, log_level: _T_LogLevel = 4) -> None:
        """
        设置日志是否输出到控制台

        Args:
            is_open: 设置日志是否输出到控制台。开关默认是打开状态。
            log_level: 控制台的日志输出等级，默认为 `4`
        """
    @staticmethod
    def setFile(file_path: str | None, log_level: _T_LogLevel = 4) -> None:
        """
        设置日志是否输出到文件

        Args:
            file_path: 设置日志输出到的文件路径。如果传入空字符串或者 `None`，则代表关闭到文件的输出。开关默认是关闭状态。
            log_level: 控制台的日志输出等级，默认为 `4`
        """
    @staticmethod
    def setPlayer(player: Player | None, log_level: _T_LogLevel = 4) -> None:
        """
        设置日志是否输出到某个玩家

        Args:
            player: 设置日志输出到的目标玩家对象。如果传入 `None`，则代表关闭到玩家的输出。开关默认是关闭状态。
            log_level: 玩家的最小日志输出等级，默认为 `4`
        """
    @staticmethod
    def setTitle(title: str) -> None:
        """
        设置自定义日志消息标头

        「标头」为日志输出条目开头的文字，用来直观地区分日志的输出源。默认消息标头为插件名。

        例如：设置自定义标头为 `LiteLoader`，则在接下来的日志输出将变为形如：

        ```log
        20:05:26 ERROR [LiteLoader] Fail to transport the player
        ```

        Args:
            title: 设置的自定义标头
        """
    @staticmethod
    def setLogLevel(level: _T_LogLevel) -> None:
        """
        统一修改日志输出等级

        Args:
            level: 日志输出等级
        """
    @staticmethod
    def log(*args: Tuple[Any]) -> None:
        """
        输出普通文本

        在输出的时候会按照原样输出。

        Args:
            args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
        """
    @staticmethod
    def debug(*args: Tuple[Any]) -> None:
        """
        输出调试信息

        Args:
            args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
        """
    @staticmethod
    def info(*args: Tuple[Any]) -> None:
        """
        输出提示信息

        Args:
            args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
        """
    @staticmethod
    def warn(*args: Tuple[Any]) -> None:
        """
        输出警告信息

        Args:
            args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
        """
    @staticmethod
    def error(*args: Tuple[Any]) -> None:
        """
        输出错误信息

        Args:
            args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
        """
    @staticmethod
    def fatal(*args: Tuple[Any]) -> None:
        """
        输出严重错误信息

        Args:
            args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
        """
