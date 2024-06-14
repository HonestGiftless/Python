# get_days_in_month()

import datetime, calendar, locale

def get_days_in_month(year, month):
    all_month = list(calendar.month_name)
    days = calendar.monthrange(year, all_month.index(month))[1]

    result = [datetime.date(year=year, month=all_month.index(month), day=i) for i in range(1, days+1)]

    return result