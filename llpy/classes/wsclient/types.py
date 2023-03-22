from typing import Literal

T_WSClientStatusOpen = Literal[0]
T_WSClientStatusClosing = Literal[1]
T_WSClientStatusClosed = Literal[2]
T_WSClientStatus = (
    T_WSClientStatusOpen | T_WSClientStatusClosing | T_WSClientStatusClosed
)
