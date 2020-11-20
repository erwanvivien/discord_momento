import discord
from discord.ext import commands


# Personnal commands
from commands import default, help, set, \
    next, week, author_name, prefix, \
    report, missing, forceupdate, test

from utils import get_content

cmds = {'': default,
        'help': help,
        'set': set,
        'next': next,
        'week': week,
        'prefix': prefix,
        'report': report,
        'missing': missing,
        'forceupdate': forceupdate,
        'test': test}


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print()
        print('==============================================')
        await client.change_presence(status=discord.Status.idle,
                                     activity=discord.Game("chronos"))

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

    async def on_reaction_add(self, reaction, user):
        if user.id in [778983226110640159, 778983263871696897]:
            return

        print(f"{user} added a {reaction.emoji}")

        # Both dev ids
        if reaction.emoji in ['✅'] and user.id in [138282927502000128, 289145021922279425] \
                and reaction.message.channel.id == 779292533595045919:
            await reaction.message.delete()

        # Both bot ids
        if reaction.emoji in ['❌'] and reaction.message.author.id in [778983226110640159, 778983263871696897]:
            await reaction.message.delete()


client = Client()
client.run(get_content("token"))
