# Вы кто такие? Я вас не звал

import csv
from datetime import date, time, datetime
from collections import namedtuple

Friend = namedtuple('Friend', ['surname', 'name', 'meeting_date', 'meeting_time'])
result = list()

with open('meetings.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file))
    
    for row in range(1, len(rows)):
        date_pattern, time_pattern = '%d.%m.%Y', '%H:%M'
        dt = datetime.strptime(rows[row][2] + " " + rows[row][3], date_pattern + " " + time_pattern)
        rows[row][2] = dt.date()
        rows[row][3] = dt.time()

        item = Friend._make(rows[row])
        result.append(item)

result = sorted(result, key=lambda item: (item.meeting_date, item.meeting_time))

for i in result:
    print(i.surname, i.name)