# num_of_sundays()

from datetime import datetime, timedelta

def num_of_sundays(year):
    first_day = datetime(year=year, month=1, day=1)
    counter = 0

    while (first_day.year == year):
        if first_day.weekday() == 6:
            counter += 1

        first_day += timedelta(days=1)
    
    return counter