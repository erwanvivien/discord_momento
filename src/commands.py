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

ARCS = ["ARCS"]

BACHELOR = ["BACHELOR"]

ING1 = ["BING B", "RIEMANN A1", "RIEMANN A2",
        "SHANNON C1", "SHANNON C2", "SHANNON C3", "SHANNON C4", "SHANNON C5",
        "TANENBAUM D1", "TANENBAUM D2", "TANENBAUM D3", "TANENBAUM D4", "TANENBAUM D5"]
MAJEURES = ["RDI", "MTI", "GISTRE", "SRS", "IMAGE",
            "SIGL", "SCIA", "TCOM", "GITM", "IMAGE"]
APPRENTISAGE = ["APPING_I 1A", "APPING_I 1B", "APPING_X 1",
                "APPING_I 2A", "APPING_I 2B", "APPING_X 2",
                "APPING_I 3", "APPING_X 3"]
PREPA = ["INFO2API", "INFOS1A", "INFOS1B", "INFOS1C", "INFOS1D", "INFOS1E", "INFOS1F",
         "INFOS2A", "INFOS2B", "INFOS2C", "INFOS2D", "INFOS2E", "INFOS2F",
         "INFOS3A", "INFOS3B", "INFOS3C", "INFOS3D", "INFOS3E",
         "INFOS4A", "INFOS4B", "INFOS4C", "INFOS4D"]
PREPA_SHARP = ["INFOS1#A1", "INFOS2#A1",
               "INFOS2#A2", "INFOS3#A1", "INFOS3#A2"]
INTER = ["GITM S8 [FP]", "GITM S9 [FP]", "SDM S8 [FP]", "SDM S9 [FP]",
         "SNS S8 [FP]", "SNS S9 [FP]", "Harmonization Semester S7 [FP]",
         "Excellence [FP]", "Excellence [SP]", "Foundation [FP]", "Foundation [SP]",
         "Computer Security [FP]", "Computer Security [SP]", "Data Science and Analytics [FP]", "Data Science and Analytics [SP]",
         "Fundamental for CS [FP]", "Fundamental for DSA [FP]", "Fundamental for ISM [FP]", "Fundamental for SE [FP]",
         "Fundamental for CS [SP]", "Fundamental for DSA [SP]", "Fundamental for ISM [SP]", "Fundamental for SE [SP]",
         "ISManagement [FP]", "ISManagement [SP]", "Software Engineering [FP]", "Software Engineering [SP]"]

EPITA = ARCS + BACHELOR + ING1 + MAJEURES + \
    APPRENTISAGE + PREPA + INTER

ALL = {el.lower(): el for el in ALL_list}

# print(ALL)


async def error_message(message, text="Please check ``help`` for more information"):
    embed = discord.Embed(title="Wrong arguments",
                          colour=discord.Colour(0x42aff2),
                          description=text,
                          url="https://github.com/erwanvivien/momento#how-to-use-it")
    await message.channel.send(embed=embed)


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
    if not args or len(args) != 1:
        return await error_message(message)


async def missing(self, message, args):
    if not args or len(args) != 1:
        return await error_message(message)


async def forceupdate(self, message, args):
    # Only bot owner can do this command
    # 138282927502000128 => Lycoon#7542
    # 289145021922279425 => Xiaojiba#1407

    if not (message.author.id in [289145021922279425, 138282927502000128]):
        return await error_message(message)

    if not args:
        arg = 'ALL'
    else:
        arg = ' '.join(args)
        if not arg in ALL:
            return await error_message(message, f"{arg} not found")

    print("You're admin")
    logging.warning("Started @ {}".format(time.strftime("%c")))
    for d in [OUTPUT, CALDIR]:
        if not os.path.isdir(d):
            os.mkdir(d)

    promo = get_year()

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for i in ALL:
            executor.submit(get_calendar, promo, i)

    # update_index()
    logging.warning("Finished @ {}".format(time.strftime("%c")))

    embed = discord.Embed(title=f"Update was done for {arg}",
                          colour=discord.Colour(0x42aff2))
    await message.channel.send(embed=embed)


async def help(self, message, args):
    # TODO: Get prefix from the database
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

    message = await message.channel.send(embed=embed)
    await message.add_reaction(emoji='✅')

    def check(reaction, user):
        return user.id != message.user.id and reaction.emoji in ['✅']

    try:
        reaction, user = await self.wait_for('reaction_add', timeout=15, check=check)
    except:
        return

    if reaction.emoji == '✅':
        await message.delete()
