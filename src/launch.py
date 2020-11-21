import discord
from discord.ext import commands

# Personnal commands
from commands import default, help, set, next, \
    week, author_name, prefix, report, missing, \
    test, error_message, settings, \
    BOT_IDS, DEV_IDS, REPORT_CHANN_ID  # , update  , forceupdate

from utils import get_content
from database import db_exists, db_adduser, db_exec, db_create

COMMANDS = {
    '': default,
    'help': help,
    'set': set,
    'next': next,
    'week': week,
    'prefix': prefix,
    'report': report,
    'missing': missing,
    'test': test,
    'settings': settings,
    # 'forceupdate': forceupdate,
}

# Discord bot token
token = get_content("token")


class Client(discord.Client):
    async def on_ready(self):
        print('[Momento] Logged on as {0}'.format(self.user))
        print('---------------------------------------')

        await client.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                name="Chronos",
                type=discord.ActivityType.watching))

    async def on_message(self, message):
        if message.author.id in BOT_IDS:
            return

        split = message.content.split(' ', 1)  # separate mom?[cmd] from args
        cmd = split[0]
        args = split[1].split(' ') if len(split) > 1 else None

        # Retrieve user from database and create if non-existing
        user = db_exists(message.author.id)
        if not user:
            db_adduser(message.author.id)
            prefix = "?"  # default prefix
        else:
            prefix = user[1]  # custom user prefix

        # Check if a bot command
        if not cmd.startswith(f"mom{prefix}"):
            return

        # Debugging stuff
        name = author_name(message.author)
        print(f"{name} issued {cmd} command. <{args}>")

        try:
            suffix = cmd[4:]  # Get command suffix
            cur_cmd = COMMANDS[suffix]
            await cur_cmd(self, message, args)
        except Exception as error:
            print(error)
            if not cur_cmd:
                return await error_message(message, title=f"Unknown command '{suffix}'")
            else:
                return await error_message(message, title=f"The command {suffix} failed...",
                                           desc=f"Please use ``mom{prefix}report`` if you think it's an unexpected behaviour")

    async def on_reaction_add(self, reaction, user):
        if user.id in BOT_IDS:
            return

        # For debugging purposes
        # print(f"{user} added a {reaction.emoji}")

        # Both dev ids
        if reaction.emoji in ['✅'] and user.id in DEV_IDS \
                and reaction.message.channel.id == REPORT_CHANN_ID:
            await reaction.message.delete()

        # Both bot ids
        if reaction.emoji in ['❌'] and reaction.message.author.id in BOT_IDS:
            await reaction.message.delete()


db_create()
client = Client()
client.run(token)
