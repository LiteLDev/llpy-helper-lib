from typing import Callable, Literal

_T_Event = Literal[
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
_T_EventCallback = Callable[..., bool | None]

def listen(event: _T_Event, callback: _T_EventCallback) -> bool:
    """
    注册监听器

    Args:
        event: 要监听的事件名
        callback: 注册的监听函数
            当指定的事件发生时，BDS会调用你给出的监听函数，并传入相应的参数

    Returns:
        是否成功监听事件
    """
