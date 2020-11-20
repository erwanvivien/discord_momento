import discord
import time
import datetime


GROUPS = ["GRA", "GRB", "APPINGI1", "APPINGI2", "APPINGX1", "APPINGX2",
          "APPINGX3", "BING B", "RIEMANN A1", "RIEMANN A2",
          "SHANNON C1", "SHANNON C2", "SHANNON C3", "SHANNON C4", "SHANNON C5",
          "TANENBAUM D1", "TANENBAUM D2", "TANENBAUM D3", "TANENBAUM D4", "TANENBAUM D5"]

MAJORS = ["CSI", "MTI", "GISTRE", "SRS",
          "SIGL", "SCIA", "TCOM", "GITM", "IMAGE"]


async def error_message(message):
    embed = discord.Embed(title="Wrong arguments",
                          colour=discord.Colour(0x42aff2),
                          description="Please check ``help`` for more information",
                          url="https://github.com/erwanvivien/momento#how-to-use-it")
    await message.channel.send(embed=embed)
    return 1


def author_name(author):
    name = author.nick
    if not name:
        name = author.name
    return name


async def default(self, message, args):
    if args:
        return await error_message(message)
    return 0


async def forceupdate(selft, message, args):
    logging.warning("Started @ {}".format(time.strftime("%c")))
    for d in [OUTPUT, CALDIR]:
        if not os.path.isdir(d):
            os.mkdir(d)

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in MAJORS:
            executor.submit(get_calendar, ASSISTANT_PROM, i)
        for i in GROUPS:
            executor.submit(get_calendar, STUDENT_PROM, i)

    update_index()
    logging.warning("Finished @ {}".format(time.strftime("%c")))


async def set(self, message, args):
    if not args or len(args) != 1:
        return await error_message(message)
    return 0


async def next(self, message, args):
    if args:
        return await error_message(message)
    return 0


async def week(self, message, args):
    if not args or len(args) >= 2 or not args[0].isdigit():
        return await error_message(message)
    return 0


async def prefix(self, message, args):
    if not args or len(args) != 1:
        return await error_message(message)
    return 0


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
