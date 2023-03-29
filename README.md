# LLSE-Python Helper Lib

[![wakatime](https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/dcd72d53-ac99-4567-a96a-e3de0d0b6836.svg)](https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/dcd72d53-ac99-4567-a96a-e3de0d0b6836)

## Developing……

## Install

Use `pdm` to install, then you can import it in your plugin

```shell
pdm add llpy-helper-lib
```

or you can use lip

```shell
lip i github.com/lgc-LLSEDev/llpy-helper-lib
```

## Usage

```py
from typing import cast

# you can input any ll's built-ins from `llpy`
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
from llpy.types import T_CommandCallbackResult

# you can input some utils from `llpy.utils`
from llpy.utils import command_callback, listener

# register a listener
mc.listen("onServerStarted", lambda: colorLog("green", "The Server Started!"))


# or you can use the decorator from `llpy.utils`
@listener("onConsoleCmd")
def _(cmd: str):
    logger.info(f'You typed "{cmd}"')


# register a command
cmd = mc.newCommand("testcmd", "A Test Command", PermType.Any)
cmd.optional("input", ParamType.RawText)
cmd.overload(["input"])


# set callback using `command_callback` decorator from `llpy.utils`
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
        form = mc.newSimpleForm().setTitle("Test Form").setContent(tip)
        player.sendForm(form, lambda _, __: None)

    else:
        # if not, send output to console
        out.success(tip) if arg else out.error(tip)

    return True


cmd.setup()  # set up it


# and more...

# set plugin metadata
ll.registerPlugin(
    "test",
    "test",
    [0, 0, 1, Version.Dev],
    {"Author": "student_2333"},
)
```
