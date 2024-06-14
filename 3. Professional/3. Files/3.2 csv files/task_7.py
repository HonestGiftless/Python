# Popular domains

import csv

result = list()

result_dict = dict()

with open('data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')

    for row in rows:
        domain = row["email"].split('@')[1] # outlook.com
        if domain not in result_dict.keys():
            result_dict[domain] = 1
        else:
            result_dict[domain] += 1

for k, v in result_dict.items():
    result.append([k, v])

result = sorted(result, key=lambda item: (item[1], item[0]))
header = ["domain", "count"]

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    for i in result:
        writer.writerow(i)