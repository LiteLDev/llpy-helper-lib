from typing import Any, Callable, Literal, NoReturn, overload

from llpy import LLSE_Command, LLSE_CustomForm, LLSE_SimpleForm, ParticleSpawner
from llpy.types import T_PermType

class mc:
    """MC API"""

    def __init__(self) -> NoReturn: ...

    # region listen
    @overload
    @staticmethod
    def listen(
        event: Literal["onServerStarted"],
        callback: Callable[[], Any],
    ) -> bool:
        """
        注册监听器

        服务器启动完毕 监听

        拦截事件：不可以拦截

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onConsoleCmd"],
        callback: Callable[[str], Any],
    ) -> bool:
        """
        注册监听器

        服务端执行后台命令 监听

        拦截事件：函数返回 `False`

        Callback Args:
            cmd (str): 执行的后台命令

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    # endregion

    @staticmethod
    def getBDSVersion(): ...
    @staticmethod
    def getServerProtocolVersion(): ...
    @staticmethod
    def runcmd(): ...
    @staticmethod
    def runcmdEx(): ...
    @overload
    @staticmethod
    def newCommand(cmd: str, desc: str) -> LLSE_Command:
        """
        注册一条顶层命令

        默认指令权限 `PermType.GameMasters`

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本

        Returns:
            指令对象
        """
    @overload
    @staticmethod
    def newCommand(cmd: str, desc: str, perm: T_PermType) -> LLSE_Command:
        """
        注册一条顶层命令

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本
            perm: 指令执行所需权限（`PermType`）

        Returns:
            指令对象
        """
    @overload
    @staticmethod
    def newCommand(
        cmd: str,
        desc: str,
        perm: T_PermType,
        flag: int,
    ) -> LLSE_Command:
        """
        注册一条顶层命令

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本
            perm: 指令执行所需权限（`PermType`）
            flag: 请输入 `0x80`

        Returns:
            指令对象
        """
    @overload
    @staticmethod
    def newCommand(
        cmd: str,
        desc: str,
        perm: T_PermType,
        flag: int,
        alias: str,
    ) -> LLSE_Command:
        """
        注册一条顶层命令

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本
            perm: 指令执行所需权限（`PermType`）
            flag: 请输入 `0x80`
            alias: 命令的别名

        Returns:
            指令对象
        """
    @staticmethod
    def broadcast(): ...
    @staticmethod
    def getPlayer(): ...
    @staticmethod
    def getOnlinePlayers(): ...
    @staticmethod
    def getAllEntities(): ...
    @staticmethod
    def getEntities(): ...
    @staticmethod
    def newItem(): ...
    @staticmethod
    def spawnMob(): ...
    @staticmethod
    def cloneMob(): ...
    @staticmethod
    def spawnItem(): ...
    @staticmethod
    def spawnSimulatedPlayer(): ...
    @staticmethod
    def explode(): ...
    @staticmethod
    def getBlock(): ...
    @staticmethod
    def setBlock(): ...
    @staticmethod
    def spawnParticle(): ...
    @staticmethod
    def newSimpleForm() -> LLSE_SimpleForm:
        """
        创建普通表单构建器对象

        Returns:
            新创建的普通表单构建器对象
        """
    @staticmethod
    def newCustomForm() -> LLSE_CustomForm:
        """
        创建自定义表单构建器对象

        Returns:
            新创建的自定义表单构建器对象
        """
    @staticmethod
    def setMotd(): ...
    @staticmethod
    def sendCmdOutput(): ...
    @staticmethod
    def newIntPos(): ...
    @staticmethod
    def newFloatPos(): ...
    @staticmethod
    def getDisplayObjective(): ...
    @staticmethod
    def clearDisplayObjective(): ...
    @staticmethod
    def getScoreObjective(): ...
    @staticmethod
    def newScoreObjective(): ...
    @staticmethod
    def removeScoreObjective(): ...
    @staticmethod
    def getAllScoreObjectives(): ...
    @staticmethod
    def setStructure(): ...
    @staticmethod
    def getStructure(): ...
    @staticmethod
    def newParticleSpawner(
        display_radius: int,
        high_detail: bool,
        double_side: bool,
    ) -> ParticleSpawner:
        """
        生成一个粒子生成器对象

        Args:
            display_radius: 粒子显示半径
            high_detail: 需要高细节线条
            double_side: 需要双面粒子

        Returns:
            一个粒子生成器对象
        """
    @staticmethod
    def getPlayerNbt(): ...
    @staticmethod
    def setPlayerNbt(): ...
    @staticmethod
    def setPlayerNbtTags(): ...
    @staticmethod
    def deletePlayerNbt(): ...
    @staticmethod
    def getPlayerScore(): ...
    @staticmethod
    def setPlayerScore(): ...
    @staticmethod
    def addPlayerScore(): ...
    @staticmethod
    def reducePlayerScore(): ...
    @staticmethod
    def deletePlayerScore(): ...
    @staticmethod
    def getTime(): ...
    @staticmethod
    def setTime(): ...
    @staticmethod
    def getWeather(): ...
    @staticmethod
    def setWeather(): ...
    # For Compatibly
    @staticmethod
    def regPlayerCmd(): ...
    @staticmethod
    def regConsoleCmd(): ...
    @staticmethod
    def getAllScoreObjective(): ...
    @staticmethod
    def getDisplayObjectives(): ...
    @staticmethod
    def crash(): ...
    @staticmethod
    def setMaxPlayers(): ...

# TODO
