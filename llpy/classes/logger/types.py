from typing import Literal

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
