# Moscow Wi-Fi

import csv

result = list()
result_dict = dict()

with open('wifi.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    for row in rows:
        if row["district"] not in result_dict.keys():
            result_dict[row["district"]] = int(row["number_of_access_points"])
        else:
            result_dict[row["district"]] += int(row["number_of_access_points"])

for k, v in result_dict.items():
    result.append([k, v])

result = sorted(result, key=lambda item: (-item[1], item[0]))

for i in result:
    print(*i, sep=': ')