import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    weekday = date.weekday()
    month = date.month_name()
    return calendar.day_name[weekday]

day = weekday_of_birth_date(date(1965, 4, 4))
print(day)
