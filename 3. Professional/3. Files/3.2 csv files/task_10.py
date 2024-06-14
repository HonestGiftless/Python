# The log file

import csv
from datetime import datetime

current_date = datetime.now()

result_dict = dict()

with open('name_log.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    changes = rows.fieldnames # заголовки

    for row in rows:
        if row['email'] not in result_dict.keys():
            result_dict[row['email']] = [[row['username'], datetime.strptime(row['dtime'], '%d/%m/%Y %H:%M')]]
        else:
            result_dict[row['email']].append([row['username'], datetime.strptime(row['dtime'], '%d/%m/%Y %H:%M')])

result_dict = dict(sorted(result_dict.items()))

for k, v in result_dict.items():
    if len(v) > 1:
        rrr = max(v, key=lambda x: x[1])
        max_element, max_date = rrr[0], rrr[1]
        result_dict[k] = [max_element, max_date]

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(changes)
    for k, v in result_dict.items():
        if len(v) == 1:
            result = [v[0][0], k, datetime.strftime(v[0][1], '%d/%m/%Y %H:%M')]
        else:
            result = [v[0], k, datetime.strftime(v[1], '%d/%m/%Y %H:%M')]
        writer.writerow(result)