import discord
import time
import datetime
import logging

import os
import concurrent.futures

from chronos import get_calendar, get_year


OUTPUT = '.'
CALDIR = os.path.join(OUTPUT, 'calendars')
STUDENT_PROM = get_year()
ASSISTANT_PROM = STUDENT_PROM - 2

BOT_COLOR = discord.Colour(0xFFBB74)
ERROR_COLOR = discord.Colour(0xFF0000)


async def error_message(message, text="Please check ``help`` for more information"):
    embed = discord.Embed(title="Wrong arguments",
                          colour=ERROR_COLOR,
                          description=text,
                          url="https://github.com/erwanvivien/momento#how-to-use-it")
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')


def author_name(author):
    name = author.nick
    if not name:
        name = author.name
    return name


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
    if not args or len(args) != 1:
        return await error_message(message)


async def report(self, message, args):
    REPORT_CHANN = self.get_channel(779292533595045919)
    if not args:
        return await error_message(message)

    arg = ' '.join(args)

    embed = discord.Embed(title=f"Thanks a lot for reporting this bug ! ❤️",
                          # description=f"{message.author}'s full report:\n{arg}",
                          colour=BOT_COLOR)
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')

    embed = discord.Embed(title=f"⚠️   >REPORT<   ⚠️",
                          description=f"{message.author}'s full report:\n{arg}",
                          colour=ERROR_COLOR)
    msg = await REPORT_CHANN.send(embed=embed)

    await msg.add_reaction(emoji='✅')
    await msg.add_reaction(emoji='🚧')


async def missing(self, message, args):
    REPORT_CHANN = self.get_channel(779292533595045919)
    if not args:
        return await error_message(message)
    embed = discord.Embed(title=f"Thanks a lot for reporting this bug ! ❤️",
                          # description=f"{message.author}'s full report:\n{arg}",
                          colour=BOT_COLOR)
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')

    for arg in args:
        embed = discord.Embed(title=f"⚠️   >REPORT<   ⚠️",
                              description=f"{message.author}'s full report:\nMISSING ``{arg}``'s group",
                              colour=ERROR_COLOR)
        msg = await REPORT_CHANN.send(embed=embed)

        await msg.add_reaction(emoji='✅')
        await msg.add_reaction(emoji='🚧')


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

    embed = discord.Embed(title="All the doc",
                          colour=discord.Colour(0x42aff2),
                          url="https://github.com/erwanvivien/momento#how-to-use-it",
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(
        url="https://raw.githubusercontent.com/erwanvivien/momento/master/docs/momento-icon.png")
    embed.set_footer(
        text="Momento",
        icon_url="https://raw.githubusercontent.com/erwanvivien/momento/master/docs/momento-icon.png")

    for cmd in cmds:
        embed.add_field(
            name=f'mom{prefix}{cmd[0]}', value=cmd[1], inline=True)

    msg = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji='❌')


async def test(self, message, args):
    # Only bot owner can do this command
    # 138282927502000128 => Lycoon#7542
    # 289145021922279425 => Xiaojiba#1407

    if not (message.author.id in [289145021922279425, 138282927502000128]):
        return await error_message(message)
    await message.channel.send("Did nothing :)")
