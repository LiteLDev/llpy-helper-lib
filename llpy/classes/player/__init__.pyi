from typing import NoReturn, overload

from typing_extensions import deprecated

from llpy import (
    DirectionAngle,
    FloatPos,
    IntPos,
    LLSE_Entity,
    NativePointer,
    NbtCompound,
)
from llpy.types import T_DimID, T_Number, T_PosType

from .types import T_GameMode, T_PermLevel, T_PlayerInventory

class LLSE_Player:
    """玩家对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """玩家名"""
    @property
    def pos(self) -> FloatPos:
        """玩家视角高度坐标"""
    @property
    def feetPos(self) -> FloatPos:
        """玩家腿部所在坐标（游戏内显示的方块坐标）"""
    @property
    def blockPos(self) -> IntPos:
        """玩家所在的方块坐标"""
    @property
    def lastDeathPos(self) -> IntPos:
        """玩家上次死亡的坐标"""
    @property
    def realName(self) -> str:
        """玩家的真实名字"""
    @property
    def xuid(self) -> str:
        """玩家 XUID 字符串"""
    @property
    def uuid(self) -> str:
        """玩家 UUID 字符串"""
    @property
    def permLevel(self) -> T_PermLevel:
        """玩家的操作权限等级"""
    @property
    def gameMode(self) -> T_GameMode:
        """玩家的游戏模式"""
    @property
    def canSleep(self) -> bool:
        """玩家是否可以睡觉"""
    @property
    def canFly(self) -> bool:
        """玩家是否可以飞行"""
    @property
    def canBeSeenOnMap(self) -> bool:
        """玩家是否可以在地图上看到"""
    @property
    def canFreeze(self) -> bool:
        """玩家是否可以冻结"""
    @property
    def canSeeDaylight(self) -> bool:
        """玩家是否能看到日光"""
    @property
    def canShowNameTag(self) -> bool:
        """玩家是否可以显示姓名标签"""
    @property
    def canStartSleepInBed(self) -> bool:
        """玩家是否可以开始在床上睡觉"""
    @property
    def canPickupItems(self) -> bool:
        """玩家是否可以拾取物品"""
    @property
    def maxHealth(self) -> int:
        """玩家最大生命值"""
    @property
    def health(self) -> int:
        """玩家当前生命值"""
    @property
    def inAir(self) -> bool:
        """玩家当前是否悬空"""
    @property
    def inWater(self) -> bool:
        """玩家当前是否在水中"""
    @property
    def inLava(self) -> bool:
        """玩家是否在熔岩中"""
    @property
    def inRain(self) -> bool:
        """玩家是否在淋雨"""
    @property
    def inSnow(self) -> bool:
        """玩家是否在雪中"""
    @property
    def inWall(self) -> bool:
        """玩家是否在墙上"""
    @property
    def inWaterOrRain(self) -> bool:
        """玩家是否在水中或雨中"""
    @property
    def inWorld(self) -> bool:
        """玩家是否在世界内"""
    @property
    def inClouds(self) -> bool:
        """玩家是否在云层上"""
    @property
    def speed(self) -> float:
        """玩家当前速度"""
    @property
    def direction(self) -> DirectionAngle:
        """玩家当前朝向"""
    @property
    def uniqueId(self) -> str:
        """玩家（实体的）唯一标识符"""
    @property
    def langCode(self) -> str:
        """玩家设置的语言的标识符(形如 `zh_CN`)"""
    @property
    def isLoading(self) -> bool:
        """玩家是否正在加载"""
    @property
    def isInvisible(self) -> bool:
        """玩家是否隐身中"""
    @property
    def isInsidePortal(self) -> bool:
        """玩家是否在传送门中"""
    @property
    def isHurt(self) -> bool:
        """玩家是否受伤"""
    @property
    def isTrusting(self) -> bool:
        """玩家是否受信任"""
    @property
    def isTouchingDamageBlock(self) -> bool:
        """玩家是否在能造成伤害的方块上"""
    @property
    def isHungry(self) -> bool:
        """玩家是否饿了"""
    @property
    def isOnFire(self) -> bool:
        """玩家是否着火"""
    @property
    def isOnGround(self) -> bool:
        """玩家是否在地上"""
    @property
    def isOnHotBlock(self) -> bool:
        """玩家是否在高温方块上（岩浆等）"""
    @property
    def isTrading(self) -> bool:
        """玩家是否在交易"""
    @property
    def isAdventure(self) -> bool:
        """玩家是否是冒险模式"""
    @property
    def isGliding(self) -> bool:
        """玩家是否在滑行"""
    @property
    def isSurvival(self) -> bool:
        """玩家是否是生存模式"""
    @property
    def isSpectator(self) -> bool:
        """玩家是否是旁观模式"""
    @property
    def isRiding(self) -> bool:
        """玩家是否在骑行"""
    @property
    def isDancing(self) -> bool:
        """玩家是否在跳舞"""
    @property
    def isCreative(self) -> bool:
        """玩家是否是创造模式"""
    @property
    def isFlying(self) -> bool:
        """玩家是否在飞行"""
    @property
    def isSleeping(self) -> bool:
        """玩家是否正在睡觉"""
    @property
    def isMoving(self) -> bool:
        """玩家是否正在移动"""
    @property
    def isSneaking(self) -> bool:
        """玩家是否正在潜行"""
    def isOP(self) -> bool:
        """
        判断玩家是否为 OP

        Returns:
            玩家是否为 OP
        """
    def setPermLevel(self, level: T_PermLevel) -> bool:
        """
        修改玩家操作权限

        Args:
            level: 目标操作权限等级

        Returns:
            是否成功修改
        """
    def setGameMode(self, mode: T_GameMode) -> bool:
        """
        修改玩家游戏模式

        Args:
            mode: 目标游戏模式

        Returns:
            是否成功修改
        """
    def runcmd(self, cmd: str) -> bool:
        """
        以某个玩家身份执行一条命令

        Args:
            cmd: 待执行的命令

        Returns:
            是否执行成功
        """
    @overload
    def teleport(self, pos: T_PosType) -> bool:
        """
        传送玩家至指定位置

        保持传送前朝向

        Args:
            pos: 目标位置坐标

        Returns:
            是否成功传送
        """
    @overload
    def teleport(self, pos: T_PosType, rot: DirectionAngle) -> bool:
        """
        传送玩家至指定位置

        Args:
            pos: 目标位置坐标
            rot: 传送后玩家的朝向

        Returns:
            是否成功传送
        """
    @overload
    def teleport(
        self,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> bool:
        """
        传送玩家至指定位置

        保持传送前朝向

        Args:
            x: 目标位置 X 坐标
            y: 目标位置 Y 坐标
            z: 目标位置 Z 坐标
            dim_id: 目标维度 ID

        Returns:
            是否成功传送
        """
    @overload
    def teleport(
        self,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
        rot: DirectionAngle,
    ) -> bool:
        """
        传送玩家至指定位置

        Args:
            x: 目标位置 X 坐标
            y: 目标位置 Y 坐标
            z: 目标位置 Z 坐标
            dim_id: 目标维度 ID
            rot: 传送后玩家的朝向

        Returns:
            是否成功传送
        """
    def kill(self) -> bool:
        """
        杀死玩家

        Returns:
            是否成功执行
        """
    @overload
    def kick(self) -> bool:
        """
        断开玩家连接

        Returns:
            是否成功断开连接
        """
    @overload
    def kick(self, msg: str) -> bool:
        """
        断开玩家连接

        Args:
            msg: 被踢出玩家出显示的断开原因

        Returns:
            是否成功断开连接
        """
    @overload
    def disconnect(self) -> bool:
        """
        断开玩家连接

        Returns:
            是否成功断开连接
        """
    @overload
    def disconnect(self, msg: str) -> bool:
        """
        断开玩家连接

        Args:
            msg: 被踢出玩家出显示的断开原因

        Returns:
            是否成功断开连接
        """
    def tell(self) -> VALUE: ...
    def talkAs(self) -> VALUE: ...
    def sendText(self) -> VALUE: ...
    def setTitle(self) -> VALUE: ...
    def rename(self) -> VALUE: ...
    def setFire(self) -> VALUE: ...
    def stopFire(self) -> VALUE: ...
    def transServer(self) -> VALUE: ...
    def crash(self) -> VALUE: ...
    def hurt(self) -> VALUE: ...
    def heal(self) -> VALUE: ...
    def setHealth(self) -> VALUE: ...
    def setMaxHealth(self) -> VALUE: ...
    def setAbsorption(self) -> VALUE: ...
    def setAttackDamage(self) -> VALUE: ...
    def setMaxAttackDamage(self) -> VALUE: ...
    def setFollowRange(self) -> VALUE: ...
    def setKnockbackResistance(self) -> VALUE: ...
    def setLuck(self) -> VALUE: ...
    def setMovementSpeed(self) -> VALUE: ...
    def setUnderwaterMovementSpeed(self) -> VALUE: ...
    def setLavaMovementSpeed(self) -> VALUE: ...
    def setHungry(self) -> VALUE: ...
    def refreshChunks(self) -> VALUE: ...
    def giveItem(self) -> VALUE: ...
    def clearItem(self) -> VALUE: ...
    def isSprinting(self) -> VALUE: ...
    def setSprinting(self) -> VALUE: ...
    def sendToast(self) -> VALUE: ...
    def distanceTo(self) -> VALUE: ...
    def distanceToSqr(self) -> VALUE: ...
    def getBlockStandingOn(self) -> VALUE: ...
    def getDevice(self) -> VALUE: ...
    def getHand(self) -> VALUE: ...
    def getOffHand(self) -> VALUE: ...
    def getInventory(self) -> VALUE: ...
    def getArmor(self) -> VALUE: ...
    def getEnderChest(self) -> VALUE: ...
    def getRespawnPosition(self) -> VALUE: ...
    def setRespawnPosition(self) -> VALUE: ...
    def refreshItems(self) -> VALUE: ...
    def getScore(self) -> VALUE: ...
    def setScore(self) -> VALUE: ...
    def addScore(self) -> VALUE: ...
    def reduceScore(self) -> VALUE: ...
    def deleteScore(self) -> VALUE: ...
    def setSidebar(self) -> VALUE: ...
    def removeSidebar(self) -> VALUE: ...
    def setBossBar(self) -> VALUE: ...
    def removeBossBar(self) -> VALUE: ...
    def addLevel(self) -> VALUE: ...
    def reduceLevel(self) -> VALUE: ...
    def getLevel(self) -> VALUE: ...
    def setLevel(self) -> VALUE: ...
    def setScale(self) -> VALUE: ...
    def resetLevel(self) -> VALUE: ...
    def addExperience(self) -> VALUE: ...
    def reduceExperience(self) -> VALUE: ...
    def getCurrentExperience(self) -> VALUE: ...
    def setCurrentExperience(self) -> VALUE: ...
    def getTotalExperience(self) -> VALUE: ...
    def setTotalExperience(self) -> VALUE: ...
    def getXpNeededForNextLevel(self) -> VALUE: ...
    def setAbility(self) -> VALUE: ...
    def getBiomeId(self) -> VALUE: ...
    def getBiomeName(self) -> VALUE: ...
    def getAllEffects(self) -> VALUE: ...
    def addEffect(self) -> VALUE: ...
    def removeEffect(self) -> VALUE: ...
    def sendSimpleForm(self) -> VALUE: ...
    def sendModalForm(self) -> VALUE: ...
    def sendCustomForm(self) -> VALUE: ...
    def sendForm(self) -> VALUE: ...
    def sendPacket(self) -> VALUE: ...
    def setExtraData(self) -> VALUE: ...
    def getExtraData(self) -> VALUE: ...
    def delExtraData(self) -> VALUE: ...
    def setNbt(self) -> VALUE: ...
    def getNbt(self) -> VALUE: ...
    def addTag(self) -> VALUE: ...
    def removeTag(self) -> VALUE: ...
    def hasTag(self) -> VALUE: ...
    def getAllTags(self) -> VALUE: ...
    def getAbilities(self) -> VALUE: ...
    def getAttributes(self) -> VALUE: ...
    def getEntityFromViewVector(self) -> VALUE: ...
    def getBlockFromViewVector(self) -> VALUE: ...
    def quickEvalMolangScript(self) -> VALUE: ...
    def getMoney(self) -> VALUE: ...
    def setMoney(self) -> VALUE: ...
    def addMoney(self) -> VALUE: ...
    def reduceMoney(self) -> VALUE: ...
    def transMoney(self) -> VALUE: ...
    def getMoneyHistory(self) -> VALUE: ...
    def isSimulatedPlayer(self) -> VALUE: ...
    def simulateSneak(self) -> VALUE: ...
    def simulateAttack(self) -> VALUE: ...
    def simulateDestroy(self) -> VALUE: ...
    def simulateDisconnect(self) -> VALUE: ...
    def simulateInteract(self) -> VALUE: ...
    def simulateRespawn(self) -> VALUE: ...
    def simulateJump(self) -> VALUE: ...
    def simulateLocalMove(self) -> VALUE: ...
    def simulateWorldMove(self) -> VALUE: ...
    def simulateMoveTo(self) -> VALUE: ...
    def simulateLookAt(self) -> VALUE: ...
    def simulateSetBodyRotation(self) -> VALUE: ...
    def simulateNavigateTo(self) -> VALUE: ...
    def simulateUseItem(self) -> VALUE: ...
    def simulateStopDestroyingBlock(self) -> VALUE: ...
    def simulateStopInteracting(self) -> VALUE: ...
    def simulateStopMoving(self) -> VALUE: ...
    def simulateStopUsingItem(self) -> VALUE: ...
    def simulateStopSneaking(self) -> VALUE: ...
    def asPointer(self) -> NativePointer: ...
    @deprecated("请使用 `LLSE_Player.isSneaking`")
    @property
    def sneaking(self) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getDevice()`")
    @property
    def ip(self) -> str: ...
    @deprecated("请使用 `LLSE_Player.setNbt()`")
    def setTag(self, nbt: NbtCompound) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getNbt()`")
    def getTag(self) -> NbtCompound: ...
    @deprecated("请使用 `LLSE_Player.setFire()`")
    def setOnFire(self, time: int) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getInventory()`")
    def removeItem(self, inventory_id: int, count: int) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getInventory()`")
    def getAllItems(self) -> T_PlayerInventory: ...
    @deprecated("请使用 `LLSE_Player.deleteScore()`")
    def removeScore(self, name: str) -> bool: ...
    @deprecated("请使用 `LLSE_Player.distanceTo()`")
    def distanceToPos(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number: ...

Player = LLSE_Player
