# Leap year

import calendar, locale

result = list()

for i in range(int(input())):
    result.append(calendar.isleap(int(input())))

print(*result, sep='\n')