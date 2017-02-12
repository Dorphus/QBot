from global_vars import *
import ErrorCode
import utils

login_channel = 'login'

async def new(message):
	server = message.server
	channel = getSetupChannel(server)
	name = await getStudentName(channel, message.author)
	group = await getStudentClass(channel, message.author)
	group = group.upper()
	role = await utils.getRole(server, group)
	
	if group[0] == 'T':
		course = await utils.getRole(server, 'TI student')
	elif group[0] == 'B':
		course = await utils.getRole(server, 'BIM student')
	
	await utils.change_nickname(message.author, name)
	await bot.client.add_roles(message.author, role, course)
	
def getSetupChannel(server):
    channel = discord.utils.find(lambda r: r.name == login_channel, server.channels)
    return channel
		
async def getStudentName(channel, author):
	await utils.send_message(channel, 'What is your name?')
	response = await utils.wait_for_message(author=author, channel=channel)
	return response.content

async def getStudentClass(channel, author):
	await utils.send_message(channel, 'What class are you in?\n e.g. BIM01')
	response = await utils.wait_for_message(author=author, channel=channel)
	return response.content

	"""
def getStudentID(channel, auathor)
	utils.send_message(channel, 'What is your student number?')
	response = await utils.wait_for_message(author=author, channel=channel)
	id = response.content
	"""