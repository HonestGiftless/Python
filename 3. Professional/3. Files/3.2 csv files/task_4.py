# Average salary

import csv

dct = dict()

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    for row in rows:
        if row['company_name'] not in dct.keys():
            dct[row['company_name']] = [int(row['salary']), 1]
        else:
            dct[row['company_name']] = [dct[row['company_name']][0] + int(row['salary']), dct[row['company_name']][1] + 1]

result = list()

for k, v in dct.items():
    avg = v[0] / v[1]
    result.append([k, avg])

sorted_data = sorted(result, key=lambda x: (x[1], x[0]))

for i in sorted_data:
    print(i[0])