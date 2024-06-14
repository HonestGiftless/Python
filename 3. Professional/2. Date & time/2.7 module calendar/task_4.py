# Day count 😉

import calendar, locale

year, month = input().split()

print(calendar.monthrange(int(year), int(month))[1])