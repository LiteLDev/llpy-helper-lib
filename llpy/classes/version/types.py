from typing import Literal

T_VersionStatusDev = Literal[0]
T_VersionStatusBeta = Literal[1]
T_VersionStatusRelease = Literal[2]
T_VersionStatus = T_VersionStatusDev | T_VersionStatusBeta | T_VersionStatusRelease
