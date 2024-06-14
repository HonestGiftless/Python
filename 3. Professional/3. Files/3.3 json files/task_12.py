# Students of the course

import json
import csv

with open('students.json', encoding='utf-8') as file, open('data.csv', 'w', encoding='utf-8', newline='') as output:
    rows = json.load(file)

    rst = [{'name': i['name'], 'phone': i['phone']} for i in rows if i['age'] >= 18 and i['progress'] >= 75]
    rst = sorted(rst, key=lambda item: item['name'])

    fields = ['name', 'phone']
    writer = csv.DictWriter(output, fields)
    
    writer.writeheader()
    writer.writerows(rst)