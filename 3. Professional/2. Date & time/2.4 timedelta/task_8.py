# Adjacent dates

from datetime import datetime

dates_list = input().split()
result_list = list()

for i in range(1, len(dates_list)):
    curr_date = datetime.strptime(dates_list[i], '%d.%m.%Y')
    prev_date = datetime.strptime(dates_list[i-1], '%d.%m.%Y')

    result_list.append(abs((curr_date - prev_date).days))

print(result_list)