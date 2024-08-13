# Pycon

import calendar

year, month = int(input()), int(input())
calen = calendar.monthcalendar(year=year, month=month)
count = 0

for i in calen:
    if i[3] != 0:
        count += 1
    if count == 4:
        day = i[3]
        break

if 1 <= month <= 9:
    month = "0" + str(month)

print(f"{day}.{month}.{year}")