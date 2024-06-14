# Sports grounds

import csv
import json

with open('playgrounds.csv', 'r', encoding='utf-8', newline='') as file, open('addresses.json', 'w', encoding='utf-8') as output:
    rows = csv.DictReader(file, delimiter=';')

    result = dict()

    for row in rows:
        if row['AdmArea'] not in result.keys():
            result[row['AdmArea']] = {row['District']: [row['Address']]}
        else:
            if row['District'] not in result[row['AdmArea']].keys():
                result[row['AdmArea']][row['District']] = [row['Address']]
            else:
                result[row['AdmArea']][row['District']] += [row['Address']]

    json.dump(result, output, indent=3, ensure_ascii=False)