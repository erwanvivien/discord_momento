import discord
import time
import datetime


def author_name(author):
    name = author.nick
    if not name:
        name = author.name
    return name


async def default(self, message, args):
    print("", end='')


async def set(self, message, args):
    if not args or len(args) != 1:
        await help(self, message, args)
        return


async def next(self, message, args):
    print("", end='')


async def week(self, message, args):
    print("", end='')


async def prefix(self, message, args):
    if not args or len(args) != 1:
        embed = discord.Embed(title="Wrong arguments",
                              colour=discord.Colour(0x42aff2),
                              description="Please check ``help`` for more information",
                              url="https://github.com/erwanvivien/momento#how-to-use-it")
        message = await message.channel.send(embed=embed)
        return


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
