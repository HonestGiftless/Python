# Pools

import json
from datetime import datetime, timedelta

result = list()

with open('pools.json', encoding='utf-8') as file:
    rows = json.load(file)

    for row in rows:
        start_time = datetime.strptime(row['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M')
        end_time = datetime.strptime(row['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M')

        start_time = timedelta(hours=start_time.hour, minutes=start_time.minute)
        end_time = timedelta(hours=end_time.hour, minutes=end_time.minute)
        
        if start_time <= timedelta(hours=10) and end_time >= timedelta(hours=12):
            result.append({'size': f"{row['DimensionsSummer']['Length']}x{row['DimensionsSummer']['Width']}", 'address': f"{row['Address']}"})

maximal_l, maximal_w = 0, 0
rst = ''

result = sorted(result, key=lambda item: (float(item['size'].split('x')[0]), float(item['size'].split('x')[1])), reverse=True)

print(result[0]['size'], result[0]['address'], sep='\n')