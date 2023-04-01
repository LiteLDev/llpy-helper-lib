<!-- markdownlint-disable MD033 MD036 -->

# LLSE-Python Helper Lib

[![wakatime](https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/dcd72d53-ac99-4567-a96a-e3de0d0b6836.svg)](https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/dcd72d53-ac99-4567-a96a-e3de0d0b6836)

A typing & util lib for LLSE Python runtime

为 LLSE Python 运行时开发的 类型提示/工具库

## Install / 安装

Use `pdm` to install as plugin dependency

使用 `pdm` 作为插件依赖安装

```shell
pdm add llpy-helper-lib
```

or you can use lip to install in global LLSE Python `site-packages` path

或者使用 `lip` 安装到全局 LLSE Python `site-packages` 目录

```shell
lip i llpy
```

## Usage / 用法

```py
from typing import cast

# you can input any ll's built-ins from `llpy`
# 可以从 `llpy` 导入所有的 LLSE 内置类
from llpy import (
    LLSE_CommandOrigin,
    LLSE_CommandOutput,
    ParamType,
    PermType,
    Version,
    colorLog,
    ll,
    logger,
    mc,
)

# you can input some types from `llpy.types`
# 可以从 `llpy.types` 导入本补全库提供的类型
from llpy.types import T_CommandCallbackResult

# you can input some utils from `llpy.utils`
# 可以从 `llpy.utils` 导入本库提供的实用函数/类
from llpy.utils import command_callback, listener

# register a listener
# 注册一个监听器
mc.listen("onServerStarted", lambda: colorLog("green", "The Server Started!"))


# or you can use the decorator from `llpy.utils`
# 也可以用 `llpy.utils` 里的装饰器注册
@listener("onConsoleCmd")
def _(cmd: str):
    logger.info(f'You typed "{cmd}"')


# register a command
# 注册一个指令
cmd = mc.newCommand("testcmd", "A Test Command", PermType.Any)
cmd.optional("input", ParamType.RawText)
cmd.overload(["input"])


# set callback using `command_callback` decorator from `llpy.utils`
# 可以使用 `llpy.utils` 里的装饰器设置指令回调函数
@command_callback(cmd)
def _(
    _,
    ori: LLSE_CommandOrigin,
    out: LLSE_CommandOutput,
    res: dict[str, T_CommandCallbackResult],
):
    arg = cast(str | None, res.get("input"))
    tip = f'§aYou inputed §r"§6§l{arg}§r"' if arg else "§cNothing inputted!"

    player = ori.player
    if player:
        # if player exec the cmd, send a form
        # 如果是玩家执行命令，发送表单
        form = mc.newSimpleForm().setTitle("Test Form").setContent(tip)
        player.sendForm(form, lambda _, __: None)

    else:
        # if not, send output to console
        # 不是玩家执行则输出到控制台
        out.success(tip) if arg else out.error(tip)

    return True


cmd.setup()  # set up it / 安装指令


# and more... / 更多...

# set plugin metadata
# 设置插件元信息
ll.registerPlugin(
    "test",
    "test",
    [0, 0, 1, Version.Dev],
    {"Author": "student_2333"},
)
```

## Contact / 联系我

QQ：3076823485  
QQ Group：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  
E-mail：<lgc2333@126.com>
Telegram: [@lgc2333](https://t.me/lgc2333)

## Sponsor / 赞助

Thank you all for your patronage! Your patronage will be my encouragement to continue creating!

感谢大家的赞助！你们的赞助将是我继续创作的动力！

- [AFDian / 爱发电](https://afdian.net/@lgc2333)
- <details>
    <summary>
      Sponsor QR Code / 赞助二维码<br />
      Alipay / WeChat Pay / QQ Pay<br />
      Click to Expand / 点击展开
    </summary>

  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)

  </details>

## Update Log / 更新日志

None / 暂无
