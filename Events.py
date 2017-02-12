import discord
from global_vars import *
import Commands
import utils

@bot.client.event
async def on_message(message):
    
    if(ValidMessageCheck(message) == True):
        try:
            command = getMessageType(message.content)
        except:
            await utils.send_message(message.channel, ErrorCode.CommandNotFound)
        await command(message)
    else:
        print('Error')

def ValidMessageCheck(message):
    if(message.author.bot or not MessageInAppropiateChannel(message.channel)):
        return False
    
    if message.content[0] == prefix:
        return True

def MessageInAppropiateChannel(channel):
    a = channel.name in bot.config.channels
    b = bot.config.include
    if(not a^b):
        return True
    else:
        return False

def getMessageType(content):
    cmd = content[1:len(content)].split()[0]
    command = None
    if cmd in Commands.CommandList:
        command = getattr(Commands, cmd)
    elif cmd in GameCommands.CommandList:
        command = getattr(GameCommands, cmd)
    else:
        raise CommandNotFound(ErrorCode.CommandNotFound)
    return command

@bot.client.event
async def on_ready():
    startupInfo()
    await bot.client.change_presence(game=discord.Game(name='Drinking Coffee...'))

def startupInfo():
    print('Logged in as')
    print(bot.name)
    print(bot.client.user.id)
    print('------')