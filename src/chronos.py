import datetime
from ics import Calendar
import requests
import re

def week_nb(off=0):
    today = datetime.datetime.today()
    return int(today.strftime("%U")) - 34 + off

# Returns whether the given event is occurring today or not
def is_today(time, today):
    #return str(time).startswith(str(today))
    return str(time).startswith(str(today))

# Returns .ICS file of a given group for the current week
def get_ics(group):
    try:
        return Calendar(requests.get(f"https://ichronos.net/feed/{group}.ics").text)
    except:
        return None

def get_class_id(event):
    uid = re.search("-[0-9]*@", str(event.uid))
    return uid.group()[1:-1]

def get_teacher(event):
    name = re.search("=[^:]*:", str(event.organizer))
    return name.group()[1:-1]