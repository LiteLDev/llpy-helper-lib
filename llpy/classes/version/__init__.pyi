from typing import Literal, NoReturn

class Version:
    """插件版本状态枚举"""

    def __init__(self) -> NoReturn: ...

    Dev: Literal[0]
    """正式发布版本（默认值）"""
    Beta: Literal[1]
    """测试版本"""
    Release: Literal[2]
    """开发版本"""
