from typing import Callable, Literal

T_EventName = Literal[
    # Player Events
    "onPreJoin",
    "onJoin",
    "onLeft",
    "onRespawn",
    "onPlayerDie",
    "onPlayerCmd",
    "onChat",
    "onChangeDim",
    "onJump",
    "onSneak",
    "onPlayerSwing",
    "onAttackEntity",
    "onAttackBlock",
    "onUseItem",
    "onUseItemOn",
    "onUseBucketPlace",
    "onUseBucketTake",
    "onTakeItem",
    "onDropItem",
    "onEat",
    "onAte",
    "onConsumeTotem",
    "onEffectAdded",
    "onEffectUpdated",
    "onEffectRemoved",
    "onStartDestroyBlock",
    "onDestroyBlock",
    "onPlaceBlock",
    "afterPlaceBlock",
    "onOpenContainer",
    "onCloseContainer",
    "onInventoryChange",
    # ""onMove"",
    "onChangeSprinting",
    "onSetArmor",
    "onUseRespawnAnchor",
    "onOpenContainerScreen",
    "onExperienceAdd",
    "onBedEnter",
    "onOpenInventory",
    # Entity Events
    "onMobDie",
    "onMobHurt",
    "onEntityExplode",
    "onProjectileHitEntity",
    "onWitherBossDestroy",
    "onEnderDragonDestroy",
    "onRide",
    "onStepOnPressurePlate",
    "onSpawnProjectile",
    "onProjectileCreated",
    "onNpcCmd",
    "onChangeArmorStand",
    "onEntityTransformation",
    # Block Events
    "onBlockInteracted",
    "onBlockChanged",
    "onBlockExplode",
    "onRespawnAnchorExplode",
    "onBlockExploded",
    "onFireSpread",
    "onCmdBlockExecute",
    "onContainerChange",
    "onProjectileHitBlock",
    "onRedStoneUpdate",
    "onHopperSearchItem",
    "onHopperPushOut",
    "onPistonTryPush",
    "onPistonPush",
    "onFarmLandDecay",
    "onUseFrameBlock",
    "onLiquidFlow",
    # Other Events
    "onScoreChanged",
    "onTick",
    "onServerStarted",
    "onConsoleCmd",
    "onConsoleOutput",
    # Economic Events
    "onMoneyAdd",
    "onMoneyReduce",
    "onMoneyTrans",
    "onMoneySet",
    "beforeMoneyAdd",
    "beforeMoneyReduce",
    "beforeMoneyTrans",
    "beforeMoneySet",
    "onFormResponsePacket",
    # Outdated Events
    "onAttack",
    "onExplode",
    "onBedExplode",
    "onMobSpawn",
    "onMobTrySpawn",
    "onMobSpawned",
    "onContainerChangeSlot",
]
"""可监听的事件类型"""

T_EventCallback = Callable[..., bool | None]
"""可用的事件监听回调类型"""

T_LogLevel = Literal[0, 1, 2, 3, 4, 5]
"""
日志输出等级

0. `Slient` - 不输出任何日志

1. `Fatal` - 仅输出 严重错误信息

2. `Error` - 输出 严重错误、错误信息

3. `Warn` - 输出 严重错误、错误、警告信息

4. `Info` - 输出 严重错误、错误、警告、提示信息

5. `Debug` - 输出 严重错误、错误、警告、提示 和 调试信息
"""
