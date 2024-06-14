# saturdays_between_two_dates()

from datetime import date

def saturdays_between_two_dates(start, end):
    st = start.toordinal()
    ed = end.toordinal()
    counter = 0

    if st < ed:
        for i in range(st, ed + 1):
            if date.fromordinal(i).weekday() == 5:
                counter += 1
    elif st > ed:
        for i in range(ed, st + 1):
            if date.fromordinal(i).weekday() == 5:
                counter += 1
    else:
        if date.fromordinal(st).weekday() == 5:
            counter += 1
    
    return counter