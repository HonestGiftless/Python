# ТЧМ

import datetime, calendar, locale

year = int(input())
result = list()

for month in range(1, 13):
    all_days = calendar.monthrange(year, month)[1]
    counter = 0

    for day in range(1, all_days + 1):
        if counter < 3:
            if calendar.weekday(year, month, day) == 3:
                counter += 1
        elif counter == 3:
            dat = datetime.date(year, month, day - 1)
            result.append(dat.strftime('%d.%m.%Y'))
            break

print(*result, sep='\n')