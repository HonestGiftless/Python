# Public catering 😰

import json, csv

types = dict()

with open('food_services.json', encoding='utf-8') as file:
    rows = json.load(file)

    for row in rows:
        if row['TypeObject'] not in types.keys():
            types[row['TypeObject']] = [{'name': row['Name'], 'size': row['SeatsCount']}]
        else:
            types[row['TypeObject']] += [{'name': row['Name'], 'size': row['SeatsCount']}]

for k, v in types.items():
    v = sorted(v, key=lambda item: item['size'], reverse=True)
    types[k] = v

types = dict(sorted(types.items(), key=lambda item: item[0]))

for k, v in types.items():
    print(f"{k}: {v[0]['name']}, {v[0]['size']}")