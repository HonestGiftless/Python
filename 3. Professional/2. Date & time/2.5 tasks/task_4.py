# The most understandable condition

from datetime import datetime, timedelta

start_date = datetime.strptime(input(), '%d.%m.%Y')
end_date = datetime.strptime(input(), '%d.%m.%Y')
result = list()

while start_date.weekday() == 0 and start_date.weekday() == 3 or (start_date.day + start_date.month) % 2 == 0:
    start_date += timedelta(days=1)

while start_date <= end_date:
    if start_date.weekday() != 0 and start_date.weekday() != 3:
            result.append(datetime.strftime(start_date, '%d.%m.%Y'))
    start_date += timedelta(days=3)
            
for i in result:
    print(i)