from typing import Literal

class DirectionAngle:
    """方向角对象"""

    def __init__(self, pitch: float, yaw: float) -> None:
        """
        创建方向角对象

        Args:
            pitch: 俯仰角（-90° ~ 90°）
            yaw: 偏航角（旋转角）
        """
    @property
    def pitch(self) -> float:
        """俯仰角（-90° ~ 90°）"""
    @pitch.setter
    def pitch(self, val: float): ...
    @property
    def yaw(self) -> float:
        """偏航角（旋转角）"""
    @yaw.setter
    def yaw(self, val: float): ...
    def toFacing(self) -> Literal[0, 1, 2, 3]:
        """
        将偏航角转换为基本朝向

        用于快速确定实体面向的大致方向

        Returns:
            `0-3`，代表 北东南西 四个基本朝向
        """
    def toString(self) -> str: ...
