# is_correct()

from datetime import date

def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except ValueError:
        return False