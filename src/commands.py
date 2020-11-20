import discord
import time
import datetime

# School part !

# Administations
ADM = ["INSCRIPTION", "JPO", "LOGISTIQUE", "LRDE", "LSE", "REUNION PARENTS",
       "REUNION PEDAGO", "RI", "Relations entreprises", "SECURESPHERE"]

# Associations
ASSO = ["AEDD", "Activ", "Antre", "BDE", "BDE ISBP", "Carréd'as", "Cast", "Cristal",
        "Cycom", "EpiTV", "EpiZode", "Epidemic", "Epimac", "Epioeno", "Episport",
        "Epitanime", "Gconfs", "ISBIMOOV", "Mhige", "Nomad", "Prologin", "Soul of sound",
        "Stratagame", "Synergie", "Unisson", "VJN"]


# All of EPITA
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
         "INFOS1#A1", "INFOS2A", "INFOS2B", "INFOS2C", "INFOS2D", "INFOS2E", "INFOS2F",
         "INFOS2#A1", "INFOS2#A2", "INFOS3A", "INFOS3B", "INFOS3C", "INFOS3D", "INFOS3E",
         "INFOS3#A1", "INFOS3#A2", "INFOS4A", "INFOS4B", "INFOS4C", "INFOS4D"]
INTER = ["GITM S8 [FP]", "GITM S9 [FP]", "SDM S8 [FP]", "SDM S9 [FP]",
         "SNS S8 [FP]", "SNS S9 [FP]", "Harmonization Semester S7 [FP]",
         "Excellence [FP]", "Excellence [SP]", "Foundation [FP]", "Foundation [SP]",
         "Computer Security [FP]", "Computer Security [SP]", "Data Science and Analytics [FP]", "Data Science and Analytics [SP]",
         "Fundamental for CS [FP]", "Fundamental for DSA [FP]", "Fundamental for ISM [FP]", "Fundamental for SE [FP]",
         "Fundamental for CS [SP]", "Fundamental for DSA [SP]", "Fundamental for ISM [SP]", "Fundamental for SE [SP]",
         "ISManagement [FP]", "ISManagement [SP]", "Software Engineering [FP]", "Software Engineering [SP]"]
SUMMER = ["Session A", "Session B", "Session C"]

EPITA = ARCS + BACHELOR + ING1 + MAJEURES + \
    APPRENTISAGE + PREPA + INTER + SUMMER

# All of EPITECH's classes
EPITECH = ["CA", "HUBS", "ISEG", "MSC", "PGT5", "PSO1", "SC",
           "TECH1", "TECH1-1", "TECH1-2", "TECH1-3", "TECH1-4", "TECH1-5",
           "TECH2", "TECH3", "TECH3S", "TECH3SI", "TECH4/5", "TECHX",
           "W@C#1", "W@C#2"]

# All of ETNA's classes
ETNA = ["ETNA"]

# All of ISBP
APPRENTIS = ["BIOTECH 3A", "BIOTECH 4A", "BIOTECH 5A"]
BIOTECH1 = ["Anglophone Biotech1", "BIOTECH1", "BT1A/BIOTECH1", "BT1B/BIOTECH1", "Biotech1 optionnel",
            "TD1/BIOTECH1", "TD2/BIOTECH1", "TD3/BIOTECH1", "TD4/BIOTECH1"]
BIOTECH2 = ["Anglophone Biotech2", "BIOTECH2", "BT2A/BIOTECH2", "BT2B/BIOTECH2", "Biotech2 optionnel",
            "TD1/BIOTECH2", "TD2/BIOTECH2", "TD3/BIOTECH2", "TD4/BIOTECH2"]
BIOTECH3 = ["BIOTECH3", "BIOTECH3 - Electif Bioprod", "BIOTECH3 - Electif Marketing",
            "BIOTECH3 - Electif RD", "BIOTECH3 / SHS Biomed", "BIOTECH3 / SHS Enviro",
            "BIOTECH3 BACTERIOLOGY A", "BIOTECH3 BACTERIOLOGY B", "BIOTECH3 BMP A", "BIOTECH3 BMP B",
            "BIOTECH3/Gp1", "BIOTECH3/Gp2", "BIOTECH3/Gp3", "BIOTECH3/Gp4", "BIOTECH3/GpA", "BIOTECH3/GpB"]
BIOTECH4 = ["BIOTECH4 Mineure Santé", "BIOTECH4 mineure agro", "BIOTECH4 mineure cosméto",
            "BIOTECH4 mineure environnement", "BIOTECH4/1R&D", "BIOTECH4/2Marketing", "BIOTECH4/3Production"]
BIOTECH5 = ["BIOTECH5", "BIOTECH5 mineure agro", "BIOTECH5 mineure cosméto", "BIOTECH5 mineure environnement",
            "BIOTECH5 mineure santé", "BIOTECH5/1R&D", "BIOTECH5/2Marketing", "BIOTECH5/3Production"]
EVENTS = ["JPO", "Réunions Vanessa PROUX", " concours ADVANCE"]
CLASSES1 = ["ANGLAIS AGP BT1", "ANGLAIS NS BT1", "BACTERIOLOGIE BT1", "BIOCHIMIE TD BT1", "BIOCHIMIE cours BT1",
            "BIODIVERSITE BT1", "BIOLOGIE TD BT1", "BIOLOGIE cours BT1", "CHIMIE BT1", "COMMUNICATION BT1", "Culture Générale BT1",
            "ECONOMIE BT1", "EPISTEMOLOGIE BT1", "INFORMATIQUE BT1", "MATHEMATIQUES BT1", "PHYSIQUE BT1", "PROJET VOLTAIRE BT1",
            "SHS BT1", "TUTORAT BIOLOGIE/BIOCHIMIE", "Tutorat ANGLAIS KF", "Tutorat ANGLAIS MB", "VIROLOGIE BT1"]
CLASSES2 = [
    "ANGLAIS GC", "ANGLAIS KF", "BACTERIOLOGIE BT2", "BIOCHIMIE (TD) BT2", "BIOCHIMIE (cours) BT2",
    "BIOLOGIE (TD) BT2", "BIOLOGIE (cours) BT2", "CHIMIE BT2", "CHIMIE ORGANIQUE BT2", "ECONOMIE BT2",
    "ELECTRONIQUE BT2", "EPISTEMOLOGIE BT2", "INFORMATIQUE BT2", "MATHEMATIQUES BT2", "SBIP",
    "SHS C.V BT2", "SHS FM BT2", "TUTORAT ANGLAIS", "VIROLOGIE BT2"]
CLASSES3 = ["BACTERIOLY", "BMP", "Bioinformatic", "Biomimetics", "Biostatistic", "Business Communication",
            "CHINOIS", "Cellular Biology", "Communication", "Culture Cellulaire", "ENGLISH", "Electif Bioprod",
            "Electif Ethics", "Electif Infrastructure", "Electif Marketing", "Electif Science and politics",
            "Elective Process Engineering", "Elective R&D", "Elective Sc and Env", "Elective Sc and Medecine",
            "Entrainement IELTS", "Enzyme Engineering", "FRENCH", "Humanities", "IELTS Training", "IMMUNOLOGIE",
            "Informatics", "JAPONAIS", "Marketing", "Mathematics", "Metabolism", "Microbiologie Industrielle",
            "Molecular Biology", "Organic Chemistry", "PHYSIOLOGY", "PLANT BIOLOGY", "Polymer Chemistry",
            "Process Engineering", "Project Management", "Reactor calculation", "SBIP", "Synthetic Biology",
            "TD PREPARATION TP"]

BIOTECH = APPRENTIS+BIOTECH1+BIOTECH+BIOTECH3 + \
    BIOTECH4+BIOTECH5+EVENTS+CLASSES1+CLASSES2+CLASSES3

ALL = ADM + ASSO + EPITA + EPITECH + ETNA + BIOTECH


async def error_message(message):
    embed = discord.Embed(title="Wrong arguments",
                          colour=discord.Colour(0x42aff2),
                          description="Please check ``help`` for more information",
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
    if not args or len(args) != 1 or not message.author.id in [289145021922279425, 138282927502000128]:
        return await error_message(message)
    print("You're admin")


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
