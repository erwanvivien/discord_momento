import discord
import time
import datetime
import logging

import os
import concurrent.futures

import database as db

ERRORS = []

DEV_IDS = [138282927502000128, 289145021922279425]
BOT_IDS = [778983226110640159, 778983263871696897]
REPORT_CHANN_ID = 779292533595045919

BOT_COLOR = discord.Colour(0xffbb74)
ERROR_COLOR = discord.Colour(0xff0000)
WARN_COLOR = discord.Colour(0xebdb34)

REPORT_LEN_THRESHOLD = 70
WRONG_USAGE = "Wrong usage in arguments"
HELP_USAGE = "Please check ``help`` for more information"
ADMIN_USAGE = "Are ye try'n to get ahead mayte ? This command's dev only"
HOWTO_URL = "https://github.com/erwanvivien/momento#how-to-use-it"
ICON = "https://raw.githubusercontent.com/erwanvivien/momento/master/docs/momento-icon.png"


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
    if args:
        return await error_message(message)


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
    prefix = '?'
    cmds = [('', "Shows today's schedule"),
            ('help', "Displays the help"),
            ('set', "Sets your default class"),
            ('next', "Shows the very next class"),
            ('week', "Shows week's schedule"),
            ('prefix', "Changes the ``?`` personnally")]

    embed = discord.Embed(
        title="Help information",
        url=HOWTO_URL,
        colour=discord.Colour(0x42aff2),
        timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url=ICON)
    embed.set_footer(text="Momento", icon_url=ICON)

    for cmd in cmds:
        embed.add_field(
            name=f'mom{prefix}{cmd[0]}', value=cmd[1], inline=True)

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
