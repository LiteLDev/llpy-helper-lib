from typing import TypedDict

from llpy.types import T_ToJsonType


class T_PermInfo(TypedDict):
    """权限信息"""

    name: str
    """权限名称"""
    enabled: bool
    """是否启用"""
    extra: dict[str, T_ToJsonType] | None
    """额外数据"""
