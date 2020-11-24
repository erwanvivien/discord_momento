import math

def get_content(file):
    file = open(file, "r")
    return file.read()


def author_name(author):
    return author.name if not author.nick else author.nick


# Utility function taking a datetime and converting it to a tuple
# It is called jointly with format_time() to be printed with format
def get_time_diff(diff):
    total_seconds = diff.seconds
    hours = math.floor(total_seconds / 3600)
    minutes = (total_seconds - hours * 3600) / 60
    seconds = (minutes % 1) * 60
    
    return (hours, math.floor(minutes), math.floor(seconds))

# Utility function called given get_time_diff() function argument
# time[0] for hours, time[1] for minutes, and time[2] for seconds
def format_time(time):
    str = ""
    if time[0] > 0:
        str += f"{time[0]}h"
    if time[0] != 0 or time[1] != 0:
        str += f"{time[1]}min"
    if time[2] != 0 and time[0] == 0:
        str += f"{time[2]}s"
    return str


BASE_URL = 'https://photos.cri.epita.fr/thumb/'

PROFESSORS = {
    # ING1
    'laskar gabriel': 'laskar_g',
    'tochon guillaume': 'guillaume.tochon',
    'verna didier': 'didier.verna',
    'duret-lutz alexandre': 'alexandre.duret-lutz',
    'Le Bail Gilles': 'gilles.le-bail',
    'Euvrard Guillaume': 'guillaume.euvrard',
    'Hatami Reza': 'reza.hatami',
    'Sztern Kévin': 'kevin.sztern',
    'Pommellet Adrien': 'adrien.pommellet',
    'De Peyronnet Anne Pierre': 'anne-pierre.de-peyronnet',
    'Rigoreau Leila': 'leila.rigoreau',
    'Marchais Edouard': 'edouard.marchais',
    'Chagnard Victor': 'victor.chagnard',
    'Fabrizio Jonathan': 'jonathan.fabrizio',
    'Frank Fuji': 'fuji.frank',
    'Schneider Valérie': '',
    'Moin Marie': 'marie.moin',
    'Arfi Jean-Luc': 'jean-luc arfi',
    'Gregores Joanna': 'joanna gregores',
    'Regragui Mohamed': 'mohamed.regragui',
    'Puybareau Elodie': 'elodie.puybareau',
    'Collod Victor': 'collod_v',
}

PROFESSORS = {key.lower(): BASE_URL + val for (key, val) in PROFESSORS.items()}

PROFESSORS['rouzel erwan'] = 'https://media-exp1.licdn.com/dms/image/C5103AQFkJG4DAi9tmA/profile-displayphoto-shrink_200_200/0?e=1611792000&v=beta&t=-FvDF9f2Z4Y9ufBolGY4NS6uv-18paBfd310DqqEc_o'
PROFESSORS['inconnu'] = 'https://i.pinimg.com/originals/ed/bf/ad/edbfad6bf79e808a880762bcb068f634.jpg'
PROFESSORS['acu'] = BASE_URL + 'theophane.vie'
PROFESSORS['dudin bashar'] = BASE_URL + 'dudin_b'
PROFESSORS['laskar gabriel'] = BASE_URL + 'laskar_g'

# for (k, v) in PROFESSORS.items():
#     print(str(k) + ': ' + str(v))
