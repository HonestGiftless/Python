# Восстановление недостающих ключей

import json

result = list()

with open('people.json') as file:
    data = json.load(file)

    all_keys = dict()
    
    for i in data:
        for k in i.keys():
            if k not in all_keys.keys():
                all_keys[k] = ''

    for i in data:
        for k in all_keys.keys():
            if k not in i.keys():
                i[k] = None
        result.append(i)

with open('updated_people.json', 'w') as file:
    data = json.dump(result, file, indent=3, sort_keys=True)