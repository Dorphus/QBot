from global_vars import *
import sys
import utils
import student
from utils import command

@command(name='test')
async def ping(message):
	await utils.send_message(message.channel, 'pong!')

@command(name='clean')
async def clean(message):
    cmd = message.content.split()
    chn = message.channel
    count = int(cmd[1])
    try:
        control = cmd[2]
    except IndexError:
        control = None
    deleted = await bot.client.purge_from(channel=chn, limit=count+1, check=control)
    string = '``Deleted {} message(s)``'.format(len(deleted)-1)
    await utils.send_message(chn, string)

@command(name='info')
async def info(message):
    to_print = bot.getInfo()
    await utils.send_message(message.channel, to_print)
	
@command(name='login')
async def login(message):
	if len(message.author.roles) > 1: #Everyone is also a role
		await utils.send_message(message.channel, 'You are already logged in!')
	else:
		await student.new(message)

@command(name='update')
async def update(message):
	bot.update()

thismodule = sys.modules[__name__]
CommandList = [method for method in dir(thismodule) if callable(getattr(thismodule, method)) and str(method)[0] != '_' and method not in excludes]