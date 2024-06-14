# Productivity

from datetime import datetime, timedelta

curr_date = datetime.strptime(input(), '%d.%m.%Y')

print(datetime.strftime(curr_date, '%d.%m.%Y'))

for i in range(2, 11):
    curr_date += timedelta(days=i)
    print(datetime.strftime(curr_date, '%d.%m.%Y'))