#!/usr/bin/env python3

import os
import datetime
import concurrent.futures
import time
import logging

import jinja2

import chronos


def get_year():
    y = datetime.datetime.now().year
    return y + 2 if datetime.datetime.now().month < 7 else y + 3


STUDENT_PROM = get_year()
ASSISTANT_PROM = STUDENT_PROM - 2
OUTPUT = '.'
CALDIR = os.path.join(OUTPUT, 'calendars')

GROUPS = ["GRA", "GRB", "APPINGI1", "APPINGI2", "APPINGX1", "APPINGX2",
          "APPINGX3", "BING B", "RIEMANN A1", "RIEMANN A2",
          "SHANNON C1", "SHANNON C2", "SHANNON C3", "SHANNON C4", "SHANNON C5",
          "TANENBAUM D1", "TANENBAUM D2", "TANENBAUM D3", "TANENBAUM D4", "TANENBAUM D5"]

MAJORS = ["CSI", "MTI", "GISTRE", "SRS",
          "SIGL", "SCIA", "TCOM", "GITM", "IMAGE"]


def get_calendar(promo, group):
    output = '{}/{}.ics'.format(CALDIR, group)
    cal = chronos.chronos(promo, group)
    with open('{}'.format(output), 'w') as out:
        out.writelines(cal)


def update_index():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('index.html')

    groups = [
        {'title': 'Groups', 'cals': GROUPS},
        {'title': 'Major', 'cals': MAJORS},
    ]

    def name_and_mtime(path):
        mtime = time.ctime(os.path.getmtime('{}/{}.ics'.format(CALDIR, path)))
        return path, mtime

    for group in groups:
        group['cals'] = map(name_and_mtime, group['cals'])

    output = template.render(groups=groups)
    with open(os.path.join(OUTPUT, "index.html"), "w") as f:
        f.write(output)


def main():
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


if __name__ == '__main__':
    main()
