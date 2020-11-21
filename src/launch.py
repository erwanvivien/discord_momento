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
    '': {'cmd': cmds.default, 'usage': "Shows today's schedule"},
    'help': {'cmd': cmds.help, 'usage': "Shows help information"},
    'set': {'cmd': cmds.set, 'usage': "Sets your default class"},
    'next': {'cmd': cmds.next, 'usage': "Shows the very next class"},
    'week': {'cmd': cmds.week, 'usage': "Shows week's schedule"},
    'prefix': {'cmd': cmds.prefix, 'usage': "Changes the ``?`` personally"},
    'report': {'cmd': cmds.report, 'usage': "Reports a bug to devs"},
    'settings': {'cmd': cmds.settings, 'usage': "Shows current user's settings"},
    'test': {'cmd': cmds.test},
    'logs': {'cmd': cmds.logs},
    'fail': {'cmd': cmds.fail},
}

# Discord bot token
token = get_content("token")


class Client(discord.Client):
    async def on_ready(self):
        print(f'[Momento] Logged on as {self.user}')
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
        prefix = db.get_prefix(message.author.id)

        # Check if a bot command
        if not cmd.startswith(f"mom{prefix}"):
            return

        # Debugging stuff
        name = author_name(message.author)
        print(f"{name} issued {cmd} command. <{args}>")

        cur_cmd = None
        try:
            suffix = cmd[4:]  # Get command suffix
            cur_cmd = COMMANDS[suffix]['cmd']
            await cur_cmd(self, message, args)
        except Exception as error:
            cmds.ERRORS += [time.ctime() + ': ' + str(error)]
            if not cur_cmd:
                return await cmds.error_message(message, title=f"Unknown command '{suffix}'")
            cmd = cmds.format_cmd(prefix, "report")
            await cmds.error_message(message, 
                title=f"The command {suffix} failed...",
                desc=f"Please use ``{cmd}`` if you think it's an unexpected behaviour")

    async def on_reaction_add(self, reaction, user):
        if user.id in cmds.BOT_IDS:
            return

        # Debugging stuff
        print(f"{user} added a {reaction.emoji}")

        # Both dev ids
        if reaction.emoji in ['✅'] and user.id in cmds.DEV_IDS \
                and reaction.message.channel.id == cmds.REPORT_CHANN_ID:
            await reaction.message.delete()
            
        if reaction.emoji in ['❌']:
            await reaction.message.delete()


db.create()
client = Client()
client.run(token)
