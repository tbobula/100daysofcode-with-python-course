from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    DELTA = timedelta(days=100)
    STEP = timedelta(seconds=84600)
    DATE = PYBITES_BORN
    while True:
        if DATE - PYBITES_BORN == 365:
            yield DATE
        # DATE = PYBITES_BORN + STEP
        #     yield datetime(year=DATE.year, month=PYBITES_BORN.month, day=PYBITES_BORN.day)
        # yield DATE
        DATE = DATE + STEP

dates = []
index = 0
for dat in gen_special_pybites_dates():
    print(dat)
    if index == 10:
        break
    index += 1