# fill_up_missing_dates()

from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    result_list = list()

    for i in range(len(dates)):
        dates[i] = datetime.strptime(dates[i], '%d.%m.%Y')

    maximal_day = max(dates)
    minimal_day = min(dates)


    while minimal_day <= maximal_day:
        result_list.append(datetime.strftime(minimal_day, '%d.%m.%Y'))
        minimal_day += timedelta(days=1)

    return result_list