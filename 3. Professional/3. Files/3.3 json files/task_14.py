# Exam results 🌶️

import json, csv
from datetime import datetime

result = list()
rst = dict()

with open('exam_results.csv', encoding='utf-8') as file, open('best_scores.json', 'w') as output:
    fields = ['name', 'surname', 'score', 'date_and_time', 'email']
    data = csv.DictReader(file, delimiter=',')

    for i in data:
        if f"{i['name']} {i['surname']}" not in rst.keys():
            rst[f"{i['name']} {i['surname']}"] = [{fields[2]: int(i[fields[2]]), fields[3]: i[fields[3]], fields[4]: i[fields[4]]}]
        else:
            rst[f"{i['name']} {i['surname']}"] += [{fields[2]: int(i[fields[2]]), fields[3]: i[fields[3]], fields[4]: i[fields[4]]}]

    for k, v in rst.items():
        if len(v) == 1:
            v[0]['name'] = k.split()[0]
            v[0]['surname'] = k.split()[1]
            rst_dct = {'name': v[0]['name'], 'surname': v[0]['surname'], 'best_score': v[0]['score'], 'date_and_time': v[0]['date_and_time'], 'email': v[0]['email']}
            result.append(rst_dct)
        else:
            v = sorted(v, key=lambda item: item['score'], reverse=True)
            v = sorted(v, key=lambda item: datetime.strptime(item['date_and_time'], '%Y-%m-%d %H:%M:%S'), reverse=True)
            v[0]['name'] = k.split()[0]
            v[0]['surname'] = k.split()[1]

            rst_dct = {'name': v[0]['name'], 'surname': v[0]['surname'], 'best_score': v[0]['score'], 'date_and_time': v[0]['date_and_time'], 'email': v[0]['email']}

            result.append(rst_dct)

    result = sorted(result, key=lambda item: item['email'])
    json.dump(result, output, indent=3)