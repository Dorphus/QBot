from global_vars import *

async def send_message(channel, message):
	await bot.client.send_message(channel, message)

async def wait_for_message(author=None, message=None, channel=None):
	message = await bot.client.wait_for_message(author=author, content=message, channel=channel)
	return message

async def clean(purgeChannel, count, control):
	deleted = await bot.client.purge_from(channel=purgeChannel, limit=count, check=control)
	return deleted

async def getRole(server, role):
	role = discord.utils.find(lambda r: r.name == role, server.roles)
	if role == None:
		utils.send_message('Role does not exist!')
	else:
		return role
	
async def add_role(person, role):
	if role in person.roles:
		print(person, ' already has this role!')
		return None
	await bot.client.add_roles(person, role)

async def change_nickname(person, nickname):
		await bot.client.change_nickname(person, nickname)
		
def setReadPermission(channel, user):
	overwrite = discord.PermissionOverwrite()
	overwrite.read_messages = True
	bot.client.edit_channel_permissions(channel, user, overwrite)

def setReadPermission(channel, user):
	overwrite = discord.PermissionOverwrite()
	overwrite.read_messages = False
	bot.client.edit_channel_permissions(channel, user, overwrite)

class CommandWrapper(object):
	def __init__(self, func, **kwargs):
		self.func = func
		for key in kwargs: setattr(self, key, kwargs[key])
	
	def __call__(self, message):
		return self.func(message)
	
	def __repr__(self):
		to_print = self.name
		return to_print

def command(**kwargs):
	def decorator(func):
		return CommandWrapper(func, **kwargs)
	return decorator

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False