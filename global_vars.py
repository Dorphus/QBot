import asyncio
import ErrorCode
from pathlib import Path
import discord
import threading
import shelve
from Q import *

bot = Bot()
prefix = '.'