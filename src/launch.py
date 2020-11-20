import discord
from discord.ext import commands


# Personnal commands
from commands import default, help, set, \
    next, week, author_name, prefix, \
    report, missing, forceupdate

from utils import get_content

cmds = {'': default,
        'help': help,
        'set': set,
        'next': next,
        'week': week,
        'prefix': prefix,
        'report': report,
        'missing': missing,
        'forceupdate': forceupdate}


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print()
        print('==============================================')

    async def on_message(self, message):
        line = message.content.split(' ', 1)
        cmd = line[0]
        args = line[1].split(' ') if len(line) > 1 else None

        # TODO: Grab from DB prefix
        prefix = "?"

        if not cmd.startswith(f"mom{prefix}"):
            return

        name = author_name(message.author)
        print(f"{name} > {cmd} > {args}")

        try:
            c = cmd[4:]
            retcode = await cmds[c](self, message, args)
        except Exception as error:
            return print(error)


client = Client()
client.run(get_content("token"))
