# День недели

import calendar, locale

year, month, day = input().split('-')
day_num = calendar.weekday(int(year), int(month), int(day))

print(calendar.day_name[day_num])