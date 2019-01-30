from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    DELTA = timedelta(days=100)
    STEP = timedelta(seconds=86400)
    PREVIOUSE_DATE = PYBITES_BORN
    CURRENT_DATE = PYBITES_BORN
    while True:
        if CURRENT_DATE - PREVIOUSE_DATE == DELTA:
            PREVIOUSE_DATE = CURRENT_DATE
            yield CURRENT_DATE
        if CURRENT_DATE.year != PYBITES_BORN.year  and CURRENT_DATE.month == 12 and CURRENT_DATE.day == 19:
            yield CURRENT_DATE
        CURRENT_DATE = CURRENT_DATE +  STEP

def gen_better_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)


index = 0
for d in gen_better_dates():
    print(d)
    index += 1
    if index == 10:
        break


