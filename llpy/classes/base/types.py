from typing import Literal

from .pos import FloatPos, IntPos

T_DimIDOverWorld = Literal[0]
"""维度ID | 主世界"""
T_DimIDNether = Literal[1]
"""维度ID | 下界"""
T_DimIDTheEnd = Literal[2]
"""维度ID | 末地"""
T_DimID = T_DimIDOverWorld | T_DimIDNether | T_DimIDTheEnd

T_BasicFacing = Literal[0, 1, 2, 3]
"""基本朝向。`0-3` 分别代表 北东南西 四个基本朝向"""

T_PosType = IntPos | FloatPos
T_Number = int | float
