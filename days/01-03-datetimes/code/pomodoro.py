from datetime import datetime
from datetime import timedelta
from time import sleep


def timer(second=0, minutes=0):
    counter = timedelta(seconds=second, minutes=minutes)

    start_time = datetime.now()
    print(start_time)
    while True:
        timer = datetime.now() - start_time
        if counter <= timer:
            break
        sleep(1)
    print(datetime.now())


def counter(second=0):
    while second != 0:
        print(second)
        sleep(1)
        second -= 1


counter(10)
timer(second=20, minutes=0)
