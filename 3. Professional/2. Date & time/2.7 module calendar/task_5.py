# Day count 😎

import calendar, locale

year, month = input().split()
all_month = list(calendar.month_name)

print(calendar.monthrange(int(year), all_month.index(month))[1])