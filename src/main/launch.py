import discord
from discord.ext import commands

def get_token(file):
    file = open(file, "r")
    return file.read()

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = Client()
client.run(get_token("token"))