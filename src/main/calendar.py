# import ics
# import chronos


# def get_year():
#     y = datetime.datetime.now().year
#     return y + 2 if datetime.datetime.now().month < 7 else y + 3


# STUDENT_PROM = get_year()
# ASSISTANT_PROM = STUDENT_PROM - 2
# OUTPUT = '.'
# CALDIR = os.path.join(OUTPUT, 'calendars')


# def get_calendar(promo, group):
#     output = '{}/{}.ics'.format(CALDIR, group)
#     cal = chronos.chronos(promo, group)
#     with open('{}'.format(output), 'w') as out:
#         out.writelines(cal)
