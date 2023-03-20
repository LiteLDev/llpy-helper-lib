from enum import Enum
from typing import NoReturn

class Version(Enum):
    """插件版本状态枚举"""

    def __init__(self) -> NoReturn: ...

    Dev: int
    """正式发布版本（默认值）"""
    Beta: int
    """测试版本"""
    Release: int
    """开发版本"""
