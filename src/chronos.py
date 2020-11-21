from datetime import *
import ics


def week_nb(off=0):
    today = datetime.today()
    return int(today.strftime("%U")) - 34 + off


print(week_nb())
