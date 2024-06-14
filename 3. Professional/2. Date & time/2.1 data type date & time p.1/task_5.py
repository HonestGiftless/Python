# get_min_max()

from datetime import date

def get_min_max(dates):
    if len(dates) != 0:
        res = (min(dates), max(dates))
    else:
        res = ()
    return res