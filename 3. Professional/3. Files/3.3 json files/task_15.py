# Public catering 😥

import json, csv

districts = dict()
names = dict()

with open('food_services.json', encoding='utf-8') as file:
    rows = json.load(file)

    for row in rows:
        if row['District'] not in districts.keys():
            districts[row['District']] = 1
        else:
            districts[row['District']] += 1
        
        if row['IsNetObject'].lower() == "да":
            if row['OperatingCompany'] not in names.keys():
                names[row['OperatingCompany']] = 1
            else:
                names[row['OperatingCompany']] += 1

districts_result = sorted(districts.items(), key=lambda item: item[1], reverse=True)
sorted_dictionary = dict(districts_result)
names_result = sorted(names.items(), key=lambda item: item[1], reverse=True)

print(*districts_result[0], sep=': ')
print(*names_result[0], sep=': ')