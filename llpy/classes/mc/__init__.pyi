from typing import Any, Callable, Literal, NoReturn, overload

from typing_extensions import deprecated

from llpy import (
    FloatPos,
    IntPos,
    LLSE_Block,
    LLSE_Command,
    LLSE_CustomForm,
    LLSE_Entity,
    LLSE_Item,
    LLSE_Objective,
    LLSE_Player,
    LLSE_SimpleForm,
    NbtCompound,
    ParticleSpawner,
)
from llpy.types import T_DimID, T_Number, T_PermType, T_PosType, T_ScoreDisplaySlot

from .types import (
    T_BroadcastType,
    T_ConsoleCmdCallback,
    T_PlayerCmdCallback,
    T_RunCmdExRet,
    T_StructRotationType,
    T_StructureMirrorType,
    T_TimeID,
    T_WeatherID,
)

class mc:
    """MC API"""

    def __init__(self) -> NoReturn: ...

    # TODO Listeners
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
    def getBDSVersion() -> str:
        """
        获取服务器版本号

        Returns:
            服务端版本号字符串，格式形如 `v1.17.10`
        """
    @staticmethod
    def getServerProtocolVersion() -> int:
        """
        获取服务器协议版本

        Returns:
            服务端协议版本
        """
    @staticmethod
    def runcmd(cmd) -> bool:
        """
        执行一条后台命令

        Args:
            cmd: 待执行的命令

        Returns:
            是否执行成功
        """
    @staticmethod
    def runcmdEx(cmd) -> T_RunCmdExRet:
        """
        执行一条后台命令（强化版）

        `runcmdEx` 与普通 `runcmd` 实现区别非常大，在于 Ex 版本拥有隐藏输出的机制，执行结果不会输出至控制台。
        因此如果有需要，要手动用 `log` 函数将结果输出

        Args:
            cmd: 待执行的命令

        Returns:
            命令执行结果
        """
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
    def broadcast(msg: str, msg_type: T_BroadcastType = 0) -> bool:
        """
        广播一个文本消息给所有玩家

        Args:
            msg: 待发送的文本
            msg_type: 发送的文本消息类型

        Returns:
            是否成功发送
        """
    @staticmethod
    def getPlayer(info: str) -> LLSE_Player | None:
        """
        从现有玩家获取玩家对象

        Args:
            info: 玩家的 名字 或者 XUID 或者 uniqueId

        Returns:
            生成的玩家对象。如返回值为 `None` 则表示获取玩家失败
        """
    @staticmethod
    def getOnlinePlayers() -> list[LLSE_Player]:
        """
        获取所有在线玩家

        Returns:
            在线的玩家对象列表
        """
    @staticmethod
    def getAllEntities() -> list[LLSE_Entity]:
        """
        获取当前所有已加载的实体

        Returns:
            实体对象列表
        """
    @overload
    @staticmethod
    def getEntities(pos: T_PosType, distance: float = 2.0) -> list[LLSE_Entity]: ...
    @overload
    @staticmethod
    def getEntities(
        pos: T_PosType,
        pos2: T_PosType,
        distance: float = 2.0,
    ) -> list[LLSE_Entity]: ...
    @staticmethod
    def newItem(name: str, count: int) -> LLSE_Item | None:
        """
        生成新的物品对象

        Args:
            name: 物品的标准类型名，如 `minecraft:bread`
            count: 物品堆叠数量，最大值为 `64`

        Returns:
            生成的物品对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnMob(name: str, pos: T_PosType) -> LLSE_Entity | None:
        """
        生成新生物并获取

        通过此函数，在指定的位置生成一个新生物，并获取它对应的实体对象

        Args:
            name: 生物的命名空间名称，如 `minecraft:creeper`
            pos: 生成生物的位置的坐标对象

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnMob(
        name: str,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Entity | None:
        """
        生成新生物并获取

        通过此函数，在指定的位置生成一个新生物，并获取它对应的实体对象

        Args:
            name: 生物的命名空间名称，如 `minecraft:creeper`
            x: 生成生物的位置的 X 坐标
            y: 生成生物的位置的 Y 坐标
            z: 生成生物的位置的 Z 坐标
            dim_id: 生成生物的位置的 维度 ID

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def cloneMob(entity: LLSE_Entity, pos: T_PosType) -> LLSE_Entity | None:
        """
        复制生物并获取

        通过此函数，在指定的位置复制另一个实体，并获取它对应的实体对象

        Args:
            entity: 需要复制的实体对象
            pos: 生成生物的位置的坐标对象

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def cloneMob(
        entity: LLSE_Entity,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Entity | None:
        """
        复制生物并获取

        通过此函数，在指定的位置复制另一个实体，并获取它对应的实体对象

        Args:
            entity: 需要复制的实体对象
            x: 生成生物的位置的 X 坐标
            y: 生成生物的位置的 Y 坐标
            z: 生成生物的位置的 Z 坐标
            dim_id: 生成生物的位置的 维度 ID

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnItem(item: LLSE_Item, pos: T_PosType) -> LLSE_Entity | None:
        """
        根据物品对象生成掉落物实体

        通过此函数，根据物品对象，在指定的位置生成一个同样内容的掉落物实体

        Args:
            item: 生成掉落物实体所使用的物品对象
            pos: 生成掉落物实体的位置的坐标对象

        Returns:
            生成的掉落物实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnItem(
        item: LLSE_Item,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Entity | None:
        """
        根据物品对象生成掉落物实体

        通过此函数，根据物品对象，在指定的位置生成一个同样内容的掉落物实体

        Args:
            item: 生成掉落物实体所使用的物品对象
            x: 生成掉落物实体的位置的 X 坐标
            y: 生成掉落物实体的位置的 Y 坐标
            z: 生成掉落物实体的位置的 Z 坐标
            dim_id: 生成掉落物实体的位置的 维度 ID

        Returns:
            生成的掉落物实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnSimulatedPlayer(name: str, pos: T_PosType) -> LLSE_Player | None:
        """
        创建一个模拟玩家

        Args:
            name: 模拟玩家名称
            pos: 生成模拟玩家的位置的坐标对象

        Returns:
            生成的模拟玩家对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnSimulatedPlayer(
        name: str,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Player | None:
        """
        创建一个模拟玩家

        Args:
            name: 模拟玩家名称
            x: 生成模拟玩家的位置的 X 坐标
            y: 生成模拟玩家的位置的 Y 坐标
            z: 生成模拟玩家的位置的 Z 坐标
            dim_id: 生成模拟玩家的位置的 维度 ID

        Returns:
            生成的模拟玩家对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def explode(
        pos: T_PosType,
        source: LLSE_Entity | None,
        power: float,
        explode_range: float,
        is_destroy: bool,
        is_fire: bool,
    ) -> bool:
        """
        在指定位置制造一次爆炸

        Args:
            pos: 引发爆炸的位置坐标
            source: 设置爆炸来源的实体对象，可以为 `None`
            power: 爆炸的威力值，影响爆炸的伤害大小和破坏范围
            explode_range: 爆炸的范围半径，影响爆炸的波及范围
            is_destroy: 爆炸是否破坏方块
            is_fire: 爆炸结束后是否留下燃烧的火焰

        Returns:
            是否成功制造爆炸
        """
    @overload
    @staticmethod
    def explode(
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
        source: LLSE_Entity | None,
        power: float,
        explode_range: float,
        is_destroy: bool,
        is_fire: bool,
    ) -> bool:
        """
        在指定位置制造一次爆炸

        Args:
            x: 引发爆炸的位置的 X 坐标
            y: 引发爆炸的位置的 Y 坐标
            z: 引发爆炸的位置的 Z 坐标
            dim_id: 生成模拟玩家的位置的 维度 ID
            source: 设置爆炸来源的实体对象，可以为 `None`
            power: 爆炸的威力值，影响爆炸的伤害大小和破坏范围
            explode_range: 爆炸的范围半径，影响爆炸的波及范围
            is_destroy: 爆炸是否破坏方块
            is_fire: 爆炸结束后是否留下燃烧的火焰

        Returns:
            是否成功制造爆炸
        """
    @overload
    @staticmethod
    def getBlock(pos: IntPos) -> LLSE_Block | None:
        """
        通过方块坐标获取方块对象

        Args:
            pos: 方块所在坐标

        Returns:
            生成的方块对象。如返回值为 `None` 则表示获取方块失败
        """
    @overload
    @staticmethod
    def getBlock(x: int, y: int, z: int, dim_id: T_DimID) -> LLSE_Block | None:
        """
        通过方块坐标获取方块对象

        Args:
            x: 方块所在 X 坐标
            y: 方块所在 Y 坐标
            z: 方块所在 Z 坐标
            dim_id: 方块所在 维度 ID

        Returns:
            生成的方块对象。如返回值为 `None` 则表示获取方块失败
        """
    @overload
    @staticmethod
    def setBlock(
        pos: IntPos,
        block: LLSE_Block | str | NbtCompound,
        tiledata: int = 0,
    ) -> bool:
        """
        设置指定位置的方块

        Args:
            pos: 目标方块位置
            block: 要设置成的方块对象、方块标准类型名（如 `minecraft:stone`）或 方块NBT数据
            tiledata: 方块状态值，同原版 /setblock 指令的 `tiledata`，仅通过方块类型名放置方块时有效

        Returns:
            是否成功设置
        """
    @overload
    @staticmethod
    def setBlock(
        x: int,
        y: int,
        z: int,
        dim_id: T_DimID,
        pos: IntPos,
        block: LLSE_Block | str | NbtCompound,
        tiledata: int = 0,
    ) -> bool:
        """
        设置指定位置的方块

        Args:
            x: 方块所在 X 坐标
            y: 方块所在 Y 坐标
            z: 方块所在 Z 坐标
            dim_id: 方块所在 维度 ID
            block: 要设置成的方块对象、方块标准类型名（如 `minecraft:stone`）或 方块NBT数据
            tiledata: 方块状态值，同原版 /setblock 指令的 `tiledata`，仅通过方块类型名放置方块时有效

        Returns:
            是否成功设置
        """
    @overload
    @staticmethod
    def spawnParticle(pos: T_PosType, dim_id: T_DimID, particle_type: str) -> bool:
        """
        在指定位置生成粒子效果

        Args:
            pos: 目标生成位置
            dim_id: 目标生成位置 维度 ID
            particle_type: 要生成的粒子效果名称

        Returns:
            是否成功生成
        """
    @overload
    @staticmethod
    def spawnParticle(
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
        particle_type: str,
    ) -> bool:
        """
        在指定位置生成粒子效果

        Args:
            x: 目标生成位置 X 坐标
            y: 目标生成位置 Y 坐标
            z: 目标生成位置 Z 坐标
            dim_id: 目标生成位置 维度 ID
            particle_type: 要生成的粒子效果名称

        Returns:
            是否成功生成
        """
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
    def setMotd(motd: str) -> bool:
        """
        设置服务器MOTD字符串

        Args:
            motd: 目标 MOTD 字符串

        Returns:
            是否设置成功
        """
    @staticmethod
    def setMaxPlayers(num: int) -> bool:
        """
        设置服务器最大玩家数

        Args:
            num: 最大玩家数

        Returns:
            是否设置成功
        """
    @staticmethod
    def sendCmdOutput(output: str) -> bool:
        """
        模拟产生一个控制台命令输出

        Args:
            output: 模拟产生的命令输出

        Returns:
            是否成功执行
        """
    @staticmethod
    def newIntPos(x: int, y: int, z: int, dim_id: T_DimID) -> IntPos:
        """
        生成一个整数坐标对象

        Args:
            x: X 坐标
            y: Y 坐标
            z: Z 坐标
            dim_id: 维度 ID

        Returns:
            一个整数坐标对象
        """
    @staticmethod
    def newFloatPos(x: float, y: float, z: float, dim_id: T_DimID) -> FloatPos:
        """
        生成一个浮点数坐标对象

        Args:
            x: X 坐标
            y: Y 坐标
            z: Z 坐标
            dim_id: 维度 ID

        Returns:
            一个浮点数坐标对象
        """
    @staticmethod
    def getDisplayObjective(slot: T_ScoreDisplaySlot) -> LLSE_Objective | None:
        """
        获取某个处于显示状态的计分项

        Args:
            slot: 待查询的显示槽位名称

        Returns:
            正在 `slot` 槽位显示的计分项。如果返回 `None`，则代表对应槽位未显示计分项
        """
    @staticmethod
    def clearDisplayObjective(slot: T_ScoreDisplaySlot) -> bool:
        """
        使计分项停止显示

        Args:
            slot: 显示槽位名称字符串

        Returns:
            是否清除成功
        """
    @staticmethod
    def getScoreObjective(name: str) -> LLSE_Objective | None:
        """
        获取某个已存在的计分项

        Args:
            name: 要获取的计分项名称

        Returns:
            对应的计分项对象。如果返回 `None`，则代表计分项不存在
        """
    @staticmethod
    def newScoreObjective(name: str, display_name: str) -> LLSE_Objective | None:
        """
        创建一个新的计分项

        Args:
            name: 计分项名称
            display_name: 计分项显示名称

        Returns:
            新增创建的计分项对象。如果返回 `None`，则代表创建失败
        """
    @staticmethod
    def removeScoreObjective(name: str) -> bool:
        """
        移除一个已存在的计分项

        此接口的作用类似命令 `/scoreboard objectives remove <name>`

        Args:
            name: 计分项名称

        Returns:
            是否移除成功
        """
    @staticmethod
    def getAllScoreObjectives() -> list[LLSE_Objective]:
        """
        获取所有计分项

        此接口的作用类似命令 `/scoreboard objectives list`

        Returns:
            计分板系统记录的所有计分项对象
        """
    @staticmethod
    def setStructure(
        nbt: NbtCompound,
        pos: IntPos,
        mirror: T_StructureMirrorType,
        rotation: T_StructRotationType,
    ) -> bool:
        """
        放置结构 NBT

        Args:
            nbt: NBT
            pos: 放置坐标
            mirror: 镜像模式
            rotation: 旋转角度

        Returns:
            是否成功
        """
    @staticmethod
    def getStructure(
        pos1: IntPos,
        pos2: IntPos,
        ignore_blocks: bool = False,
        ignore_entities: bool = False,
    ) -> NbtCompound:
        """
        获取结构 NBT

        Args:
            pos1: 对角坐标 1（与 `fill` 命令的 `from` 参数类似）
            pos2: 对角坐标 2（与 `fill` 命令的 `to` 参数类似）
            ignore_blocks: 忽略方块
            ignore_entities: 忽略实体

        Returns:
            NBT
        """
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
    def getPlayerNbt(uuid: str) -> NbtCompound:
        """
        获取玩家对应的 NBT 对象

        此 API 的好处是可以获取到离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID

        Returns:
            玩家的 NBT 对象
        """
    @staticmethod
    def setPlayerNbt(uuid: str, nbt: NbtCompound) -> bool:
        """
        写入玩家对应的 NBT 对象

        此 API 的好处是可以操作离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID
            nbt: NBT 对象

        Returns:
            是否成功写入
        """
    @staticmethod
    def setPlayerNbtTags(uuid: str, nbt: NbtCompound, tags: list[str]) -> bool:
        """
        覆盖玩家对应的 NBT 对象的特定 NbtTag

        此 API 的好处是可以操作离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID
            nbt: NBT 对象
            tags: 需要覆盖的 NbtTag 列表

        Returns:
            是否成功覆盖对应的 Tag
        """
    @staticmethod
    def deletePlayerNbt(uuid: str) -> bool:
        """
        从存档中删除玩家对应的 NBT 对象的全部内容

        此 API 的好处是可以操作离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID

        Returns:
            是否删除成功
        """
    @staticmethod
    def getPlayerScore(uuid: str, name: str) -> int:
        """
        获取玩家计分项的分数

        可查询离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称

        Returns:
            计分板上的数值
        """
    @staticmethod
    def setPlayerScore(uuid: str, name: str, value: int) -> bool:
        """
        设置玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称
            value: 要设置的数值

        Returns:
            是否设置成功
        """
    @staticmethod
    def addPlayerScore(uuid: str, name: str, value: int) -> bool:
        """
        增加玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称
            value: 要增加的数值

        Returns:
            是否设置成功
        """
    @staticmethod
    def reducePlayerScore(uuid: str, name: str, value: int) -> bool:
        """
        减少玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称
            value: 要减少的数值

        Returns:
            是否设置成功
        """
    @staticmethod
    def deletePlayerScore(uuid: str, name: str) -> bool:
        """
        移除玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称

        Returns:
            是否设置成功
        """
    @staticmethod
    def getTime(time_id: T_TimeID) -> int:
        """
        获取服务器游戏时间

        Args:
            time_id: 想要查询的时间

        Returns:
            获取到的时间
        """
    @staticmethod
    def setTime(tick: int) -> bool:
        """
        设置服务器游戏时间

        Args:
            tick: 想要设置的时间

        Returns:
            是否设置成功
        """
    @staticmethod
    def getWeather() -> T_WeatherID:
        """
        获取服务器天气

        Returns:
            当前天气
        """
    @staticmethod
    def setWeather(weather_id: T_WeatherID) -> bool:
        """
        设置服务器天气

        Args:
            weather_id: 想要设置的天气

        Returns:
            是否设置成功
        """
    @deprecated("请使用 `mc.newCommand()`")
    @staticmethod
    def regPlayerCmd(
        cmd: str,
        description: str,
        callback: T_PlayerCmdCallback,
        level: Literal[0, 1, 2, 3] = 0,
    ) -> bool:
        """
        注册一个新的玩家假命令

        Callback Args:
            player (LLSE_Player): 执行命令的玩家对象
            args (list[str]): 目标命令后面的参数，按空格为分界分割

        Args:
            cmd: 待注册的命令
            description: 命令描述文本
            callback: 注册的这个命令被执行时，接口自动调用的回调函数
            level: 命令的注册等级，类似于 `PermType`

        Returns:
            是否成功注册
        """
    @deprecated("请使用 `mc.newCommand()`")
    @staticmethod
    def regConsoleCmd(cmd: str, description: str, callback: T_ConsoleCmdCallback):
        """
        注册一个新的控制台假命令

        Callback Args:
            args (list[str]): 目标命令后面的参数，按空格为分界分割

        Args:
            cmd: 待注册的命令
            description: 命令描述文本
            callback: 注册的这个命令被执行时，接口自动调用的回调函数

        Returns:
            是否成功注册
        """
    @deprecated("请使用 `mc.getAllScoreObjectives()`")
    @staticmethod
    def getAllScoreObjective() -> list[LLSE_Objective]: ...
    @deprecated("请使用 `mc.getDisplayObjective()`")
    @staticmethod
    def getDisplayObjectives(slot: T_ScoreDisplaySlot) -> LLSE_Objective | None: ...
    @deprecated("已弃用，仅 DEBUG 模式下有效")
    @staticmethod
    def crash() -> bool:
        """让 BDS 崩溃"""
