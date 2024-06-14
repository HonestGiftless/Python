# csv_columns()

import csv

def csv_columns(filename):
    result = dict()

    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=',', quotechar='"')

        fields = rows.fieldnames

        for i in fields:
            result[i] = []
        
        for row in rows:
            for k, v in row.items():
                result[k].append(v)

        return result