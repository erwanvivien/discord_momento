from utils import author_name
from utils import get_content
import database as db
import discord
from discord.ext import commands
import time

# Removes circular imports
import commands as cmds

# Global that stocks every bugs (real bugs)
COMMANDS = {
    '': cmds.default,
    'help': cmds.help,
    'set': cmds.set,
    'next': cmds.next,
    'week': cmds.week,
    'prefix': cmds.prefix,
    'report': cmds.report,
    'test': cmds.test,
    'settings': cmds.settings,
    'logs': cmds.logs,
    'fail': cmds.fail
    # 'missing': cmds.missing,
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
        if message.author.id in cmds.BOT_IDS:
            return

        split = message.content.split(' ', 1)  # separate mom?[cmd] from args
        cmd = split[0]
        args = split[1].split(' ') if len(split) > 1 else None

        # Retrieve user from database and create if non-existing
        user = db.exists(message.author.id)
        if not user:
            db.adduser(message.author.id)
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
            cmds.ERRORS += [time.ctime() + ': ' + str(error)]
            if not cur_cmd:
                return await cmds.error_message(message, title=f"Unknown command '{suffix}'")
            else:
                return await cmds.error_message(message, title=f"The command {suffix} failed...",
                                                desc=f"Please use ``mom{prefix}report`` if you think it's an unexpected behaviour")

    async def on_reaction_add(self, reaction, user):
        if user.id in cmds.BOT_IDS:
            return

        # For debugging purposes
        # print(f"{user} added a {reaction.emoji}")

        # Both dev ids
        if reaction.emoji in ['✅'] and user.id in cmds.DEV_IDS \
                and reaction.message.channel.id == cmds.REPORT_CHANN_ID:
            await reaction.message.delete()

        # Both bot ids
        if reaction.emoji in ['❌'] and reaction.message.author.id in BOT_IDS:
            await reaction.message.delete()


db.create()
client = Client()
client.run(token)
