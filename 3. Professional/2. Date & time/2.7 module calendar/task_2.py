# Calendar for the month

import calendar, locale

year, month = input().split()
all_month = [i for i in calendar.month_abbr]

print(calendar.month(int(year), all_month.index(month)))