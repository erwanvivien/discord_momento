import discord
import time
import datetime
import logging

import os
import concurrent.futures

from chronos import get_calendar, get_year
from database import db_exec

OUTPUT = '.'
CALDIR = os.path.join(OUTPUT, 'calendars')
STUDENT_PROM = get_year()
ASSISTANT_PROM = STUDENT_PROM - 2
DEV_IDS = {138282927502000128, 289145021922279425}
BOT_IDS = {778983226110640159, 778983263871696897}
REPORT_CHANN_ID = 779292533595045919

BOT_COLOR = discord.Colour(0xffbb74)
ERROR_COLOR = discord.Colour(0xff0000)
WARN_COLOR = discord.Colour(0xebdb34)

REPORT_LEN_THRESHOLD = 70
WRONG_USAGE = "Wrong usage in arguments"
HELP_USAGE = "Please check ``help`` for more information"
HOWTO_URL = "https://github.com/erwanvivien/momento#how-to-use-it"
ICON = "https://raw.githubusercontent.com/erwanvivien/momento/master/docs/momento-icon.png"


async def error_message(message, title = WRONG_USAGE, desc = HELP_USAGE):
    embed = discord.Embed(title = title,
                          description = desc,
                          colour = ERROR_COLOR,
                          url = HOWTO_URL)
    await message.channel.send(embed = embed)


def author_name(author):
    return author.name if not author.nick else author.nick


async def default(self, message, args):
    if args:
        return await error_message(message)


async def set(self, message, args):
    if not args or len(args) != 1:
        return await error_message(message)

async def next(self, message, args):
    if args:
        return await error_message(message)


async def week(self, message, args):
    if not args or len(args) >= 2 or not args[0].isdigit():
        return await error_message(message)


async def prefix(self, message, args):
    if not args or len(args) != 1 or len(args[0]) > 1:
        return await error_message(message)

    if not args[0][0] in ".?,;:/!$£¤%*@+#":
        return await error_message(message)

    sql = f''' UPDATE users SET prefix = {args[0][0]} WHERE id = {message.author.id}'''
    db_exec(sql)


async def report(self, message, args):
    report_channel = self.get_channel(REPORT_CHANN_ID)
    if not args:
        return await error_message(message)

    arg = ' '.join(args)
    if len(arg) < REPORT_LEN_THRESHOLD:
        return await error_message(message, f"Reports must be at least {REPORT_LEN_THRESHOLD} characters long")

    embed = discord.Embed(
        title = f"Thanks a lot for reporting this bug ! ❤️",
        colour = BOT_COLOR)
    await message.channel.send(embed = embed)

    embed = discord.Embed(
        title = f"⚠️ New submitted report",
        description = f"(from `{message.author}`) {arg}",
        colour = WARN_COLOR)
    msg = await report_channel.send(embed = embed)

    await msg.add_reaction(emoji = '✅')
    await msg.add_reaction(emoji = '🚧')

async def missing(self, message, args):
    REPORT_CHANN = self.get_channel(REPORT_CHANN_ID)
    if not args:
        return await error_message(message)
    embed = discord.Embed(title = f"Thanks a lot for reporting this bug ! ❤️",
                          colour = BOT_COLOR)
    msg = await message.channel.send(embed = embed)

    for arg in args:
        embed = discord.Embed(title = f"⚠️   >REPORT<   ⚠️",
                              description = f"{message.author}'s full report:\nMISSING ``{arg}``'s group",
                              colour = ERROR_COLOR)
        msg = await REPORT_CHANN.send(embed = embed)

        await msg.add_reaction(emoji = '✅')
        await msg.add_reaction(emoji = '🚧')


# def update(arg=None):
#     if not arg:
#         arg = ALL['epita']

#     logging.warning("Started @ {}".format(time.strftime("%c")))
#     for d in [OUTPUT, CALDIR]:
#         if not os.path.isdir(d):
#             os.mkdir(d)

#     promo = get_year()

#     with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
#         for i in arg[0]:
#             executor.submit(get_calendar, promo, i)

#     logging.warning("Finished @ {}".format(time.strftime("%c")))

#     desc = "Other groups:\n"
#     for name in ALL:
#         desc += ' - ' + name.upper() + '\n'

#     return desc


# async def forceupdate(self, message, args):
#     # Only bot owner can do this command
#     # 138282927502000128 => Lycoon#7542
#     # 289145021922279425 => Xiaojiba#1407

#     if not (message.author.id in [289145021922279425, 138282927502000128, ]):
#         return await error_message(message)

#     try:
#         arg = (' '.join(args)).lower()
#         arg = ALL[arg]
#     except:
#         arg = ALL['epita']

#     desc = update(arg)

#     embed = discord.Embed(title=f"Updating {arg[1]}...",
#                           colour=ERROR_COLOR)
#     msg = await message.channel.send(embed=embed)

#     await msg.delete()
#     embed = discord.Embed(title=f"Update was done for {arg[1]}",
#                           description=desc,
#                           colour=BOT_COLOR)
#     msg = await message.channel.send(embed=embed)
#     await msg.add_reaction(emoji='❌')


async def help(self, message, args):
    prefix = '?'
    cmds = [('', "Shows today's schedule"),
            ('help', "Displays the help"),
            ('set', "Sets your default class"),
            ('next', "Shows the very next class"),
            ('week', "Shows week's schedule"),
            ('prefix', "Changes the ``?`` personnally")]

    embed = discord.Embed(
        title = "Help information",
        url = HOWTO_URL,
        colour = discord.Colour(0x42aff2),
        timestamp = datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url = ICON)
    embed.set_footer(text="Momento", icon_url = ICON)

    for cmd in cmds:
        embed.add_field(
            name=f'mom{prefix}{cmd[0]}', value=cmd[1], inline=True)

    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')


async def test(self, message, args):
    # Only bot owner can do this command
    # 138282927502000128 => Lycoon#7542
    # 289145021922279425 => Xiaojiba#1407

    if not (message.author.id in DEV_IDS):
        return await error_message(message)
    await message.channel.send("Did nothing :)")
