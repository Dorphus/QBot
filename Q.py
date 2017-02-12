import discord

__all__ = ['Bot']

class Bot(object):
    def __init__(self):
        self.client = discord.Client()
        self.config = Config()
        self.setInfo()
        self.loadTokens()

    def getInfo(self):
        info_string = '```prolog' + \
            '\nName: ' + self.client.user.name + \
            '\nNickname: ' + self.client.user.display_name +\
            '\nID: ' + self.client.user.id + \
            '\nMaster: ' + self.author + \
            '\nVersion: ' + self.version + \
            '\nCreated At: ' + self.client.user.created_at.strftime('%Y-%m-%d') + '```'
        return info_string

    def setInfo(self):
        d = getDictFromFile('info.txt')
        self.author = d['author']
        self.version = d['version']
        self.name = d['name']

    def loadTokens(self):
        d = getDictFromFile('tokens.txt')
        self._token = d['token']
        self.masterID = d['master']

    def update(self):
        self.config.update()

    def run(self):
        self.client.run(self._token)

class Config(object):
    def __init__(self):
        self.update()

    def update(self):
        d = getDictFromFile('config.txt')
        self.include = True if d['listmode'] == 'whitelist' else False
        self.channels = d['listfilter']

#returns a dictionary
def getDictFromFile(filename):
    d = {}
    with open(filename, 'r') as f:
        text = f.read().split('\n')
        for line in text:
            keys = line.split(' ',1)
            keys[0] = keys[0][0:-1].lower()
            d[keys[0]] = keys[1]
    return d