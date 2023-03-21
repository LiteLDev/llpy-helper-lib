# LL 类
from .classes.data import data as data
from .classes.iniconfig import IniConfigFile as IniConfigFile
from .classes.jsonconfig import JsonConfigFile as JsonConfigFile
from .classes.kvdatabase import KVDatabase as KVDatabase
from .classes.ll import ll as ll
from .classes.logger import logger as logger
from .classes.mc import mc as mc
from .classes.player import LLSE_Player as LLSE_Player
from .classes.player import Player as Player  # 别名
from .classes.system import system as system
from .classes.version import Version as Version

# 全局函数
from .functions import clearInterval as clearInterval
from .functions import colorLog as colorLog
from .functions import fastLog as fastLog
from .functions import log as log
from .functions import setInterval as setInterval
from .functions import setTimeout as setTimeout
