# Friday 13

from datetime import datetime, timedelta

start_date = datetime(year=1, month=1, day=1)
end_date = datetime(year=9999, month=12, day=31)

result = {}
for i in range(7):
    result[i] = 0

while start_date != end_date:
    if start_date.day == 13:
        result[start_date.weekday()] += 1
    start_date += timedelta(days=1)

for v in result.values():
    print(v)