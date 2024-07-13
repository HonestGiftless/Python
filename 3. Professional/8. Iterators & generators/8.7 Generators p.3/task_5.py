# years_days()

from datetime import date, timedelta

def years_days(year: int):
    day = date(year - 1, 12, 31)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        dates = (day + timedelta(i) for i in range(1, 367))
    else:
        dates = (day + timedelta(i) for i in range(1, 366))
    return dates