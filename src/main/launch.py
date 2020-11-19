import discord
from discord.ext import commands

prefix = "?"

def help():
    print("help")

def cmd2():
    print("clmd2")

cmds = {'': cmd2,'help': help}

def get_token(file):
    file = open(file, "r")
    return file.read()

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        cmd = message.content.split(' ')
        if not cmd[0].startswith("mom" + prefix):
            return
        try:
            cmds[cmd[0][4:]]()
        except:
            print(f"La commande {cmd[0]} n'existe pas")

client = Client()
client.run(get_token("token"))