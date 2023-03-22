from typing import Literal

from .pos import FloatPos, IntPos

T_DimIDOverWorld = Literal[0]
"""维度ID | 主世界"""
T_DimIDNether = Literal[1]
"""维度ID | 下界"""
T_DimIDTheEnd = Literal[2]
"""维度ID | 末地"""
T_DimID = T_DimIDOverWorld | T_DimIDNether | T_DimIDTheEnd

T_PosType = IntPos | FloatPos
T_Number = int | float
