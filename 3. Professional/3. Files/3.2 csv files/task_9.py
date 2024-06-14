# Последний день на Титанике

import csv

result = list()
result_dict = dict()

with open('titanic.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    for row in rows:
        if row["survived"] == '1' and float(row["age"]) < 18:
            if row["name"] not in result_dict.keys():
                result_dict[row["name"]] = row["sex"]

for k, v in result_dict.items():
    result.append([k, v])

result = sorted(result, key=lambda item: item[1], reverse=True)

for i in result:
    print(i[0])