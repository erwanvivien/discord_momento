import discord
import time
import datetime
import pytz
import logging

import os
import concurrent.futures

import database as db

from ics import Calendar
from chronos import get_ics, get_class_id, get_teacher, is_today

ERRORS = []
CMD_DETAILS = {
    '': {"desc": "Shows today's schedule", "usage": "[class]"},
    'next': {"desc": "Shows the very next class", "usage": "[class]"},
    'week': {"desc": "Shows week's schedule", "usage": "[class]"},
    'set': {"desc": "Sets your default class", "usage": "<class>"},
    'help': {"desc": "Shows help information", "usage": ""},
    'settings': {"desc": "Shows current user's settings", "usage": ""},
    'prefix': {"desc": "Changes the ``?`` for the user", "usage": "<prefix>"},
    'report': {"desc": "Reports a bug to the devs", "usage": "<message>"}
}

DEV_IDS = [138282927502000128, 289145021922279425]
BOT_IDS = [778983226110640159, 778983263871696897]
REPORT_CHANN_ID = 779292533595045919

BOT_COLOR = discord.Colour(0xffbb74)
ERROR_COLOR = discord.Colour(0xff0000)
WARN_COLOR = discord.Colour(0xebdb34)

DEFAULT_PREFIX = '?'
REPORT_LEN_THRESHOLD = 70
WRONG_USAGE = "Wrong usage in arguments"
HELP_USAGE = "Please check ``help`` for more information"
ADMIN_USAGE = "Are ye try'n to get ahead mayte ? This command's dev only"
HOWTO_URL = "https://github.com/erwanvivien/momento#how-to-use-it"
ICON = "https://raw.githubusercontent.com/erwanvivien/momento/master/docs/momento-icon.png"
BASE_LESSON = "https://chronos.epita.net/ade/custom/modules/plannings/eventInfo.jsp?eventId="

def format_cmd(userid, cmd):
    prefix = db.get_prefix(userid)
    return f"mom{prefix}{cmd} {CMD_DETAILS[cmd]['usage']}"

async def error_message(message, title=WRONG_USAGE, desc=HELP_USAGE):
    embed = discord.Embed(title=title,
                          description=desc,
                          colour=ERROR_COLOR,
                          url=HOWTO_URL)
    await message.channel.send(embed=embed)


async def default(self, message, args):
    if args:
        return await error_message(message)


async def set(self, message, args):
    if not args or len(args) != 1:
        return await error_message(message)


async def next(self, message, args):
    if not args:
        args = db.get_class(message.author.id)
        if not args:
            cmd = format_cmd(message.author.id, "set")
            return await error_message(message, 
                "You don't have any default class set.", 
                f"Please check the ``{cmd}`` command.")
    else:
        args = ' '.join(args)

    ics = get_ics(args)
    if not ics:
        return await error_message(message, 
            f"The class '{args}' does not exist", 
            "Please refer to existing iChronos classes.")

    now = datetime.datetime.now()
    for event in ics.timeline.start_after(now.replace(tzinfo = pytz.UTC)):
        start = datetime.datetime.fromisoformat(str(event.begin))
        end = datetime.datetime.fromisoformat(str(event.end))

        fmt = "%a %d %B"
        desc = f"Starts at **{start:%Hh%M}** and ends at **{end:%Hh%M}** on **{start.strftime(fmt)}**\n"
        desc += f"Teacher : **{get_teacher(event)}**\n"

        embed = discord.Embed(
            title = f"Next lesson is *{event.name}*",
            description = desc,
            url = BASE_LESSON + get_class_id(event),
            colour = BOT_COLOR,
            timestamp = now)
        embed.set_thumbnail(url=ICON)
        embed.set_footer(text="Momento", icon_url=ICON)
        await message.channel.send(embed=embed)

        # we only need the first lesson
        break


async def logs(self, message, args):
    if not message.author.id in DEV_IDS:
        return await error_message(message, desc=ADMIN_USAGE)

    global ERRORS
    if args and args[0] == 'clean':
        embed = discord.Embed(
            title="All errors were cleaned up",
            colour=ERROR_COLOR)
        await message.channel.send(embed=embed)
        ERRORS = []
        return

    error_string = ""
    for error in ERRORS:
        error_string += str(error) + "\n\n"

    embed = discord.Embed(
        title=error_string if error_string != "" else "No logs were found",
        description='mom?logs clean to remove all logs',
        colour=BOT_COLOR)
    await message.channel.send(embed=embed)


async def week(self, message, args):
    if not args or len(args) >= 2 or not args[0].isdigit():
        return await error_message(message)


async def prefix(self, message, args):
    if not args or len(args) != 1 or len(args[0]) > 1:
        return await error_message(message)

    if not args[0][0] in ".?,;:/!$£¤%*@+#":
        return await error_message(message)

    sql = f''' UPDATE users SET prefix = '{args[0][0]}' WHERE id = {message.author.id}'''
    db.exec(sql)

    embed = discord.Embed(
        title=f"Settings updated ✅",
        colour=BOT_COLOR)
    await message.channel.send(embed=embed)


async def settings(self, message, args):
    if args:
        return await error_message(message)

    sql = f''' SELECT * FROM users WHERE id = {message.author.id} '''
    settings = db.exec(sql)[0]

    embed = discord.Embed(
        title=f"Current settings",
        colour=BOT_COLOR)

    print(settings)

    settings = [('prefix', f'``{settings[1]}``'),
                ('class', f'``{settings[2]}``')]

    for set in settings:
        embed.add_field(name=set[0], value=set[1], inline=True)

    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')


async def report(self, message, args):
    if not args:
        return await error_message(message)

    report_channel = self.get_channel(REPORT_CHANN_ID)
    arg = ' '.join(args)
    if len(arg) < REPORT_LEN_THRESHOLD:
        return await error_message(message, f"Reports must be at least {REPORT_LEN_THRESHOLD} characters long")

    embed = discord.Embed(
        title=f"Thanks a lot for reporting this bug ! ❤️",
        colour=BOT_COLOR)
    await message.channel.send(embed=embed)

    embed = discord.Embed(
        title=f"⚠️ New submitted report",
        description=f"from `{message.author}` at {time.ctime()}\n{arg}",
        colour=WARN_COLOR)
    msg = await report_channel.send(embed=embed)

    await msg.add_reaction(emoji='✅')
    await msg.add_reaction(emoji='🚧')


async def help(self, message, args):
    prefix = DEFAULT_PREFIX
    embed = discord.Embed(
        title="Help information",
        url=HOWTO_URL,
        colour=discord.Colour(0x42aff2),
        timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url=ICON)
    embed.set_footer(text="Momento", icon_url=ICON)

    for key in CMD_DETAILS.keys():
        cmd_detail = CMD_DETAILS[key]
        embed.add_field(name=f'mom{prefix}{key}', value=cmd_detail['desc'], inline=True)

    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')


async def test(self, message, args):
    if not (message.author.id in DEV_IDS):
        return await error_message(message, desc=ADMIN_USAGE)
    await message.channel.send("Did nothing :)")


async def fail(self, message, args):
    if not (message.author.id in DEV_IDS):
        return await error_message(message, desc=ADMIN_USAGE)

    mockedObj.raiseError.side_effect = Mock(side_effect=Exception('Test'))
