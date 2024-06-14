# get_all_mondays()

import datetime, calendar, locale

def get_all_mondays(year):
    result = list()
    for month in range(1, 13):
        days_count = calendar.monthrange(year, month)[1]
        for days in range(1, days_count + 1):
            if calendar.weekday(year, month, days) == 0:
                result.append(datetime.date(year, month, days))
    
    return result