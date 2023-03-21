# LLSE-Python Helper Lib

[![wakatime](https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/dcd72d53-ac99-4567-a96a-e3de0d0b6836.svg)](https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/dcd72d53-ac99-4567-a96a-e3de0d0b6836)

## Developing……

## Install

Use `pdm` to install, then you can import it in your plugin

```shell
pdm add llpy-helper-lib
```

## Usage

```py
# you can from `llpy` import any built-ins from ll
from llpy import ll, mc, Version, logger
from llpy.utils import listen

# register a listener
mc.listen("onServerStarted", lambda: logger.info("The Server Started!"))


# or you can use the decorator from `llpy.utils`
@listen("onServerStarted")
def _():
    logger.info("The Server Started!")


# and more...

logger.info("Test Plugin Loaded!")

ll.registerPlugin(
    "test",
    "test",
    [0, 0, 1, Version.Dev],
    {
        "Author": "student_2333",
    },
)
```
