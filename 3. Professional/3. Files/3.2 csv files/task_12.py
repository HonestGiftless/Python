# Возрастание классов 🌶️

import csv

with open("student_counts.csv", 'r', encoding='utf-8', newline='') as file, open("sorted_student_counts.csv", 'w', encoding='utf-8', newline='') as output:
    rows = csv.DictReader(file, delimiter=",")
    writer = csv.writer(output)

    fields = rows.fieldnames

    classes = [fields[i].split('-') for i in range(1, len(fields))]
    classes = sorted(classes, key=lambda item: (int(item[0]), item[1]))

    result_fields = [fields[0]] + ["-".join(i) for i in classes]
    writer.writerow(result_fields)

    for row in rows:
        result = dict()
        result_lst = list()
        for j in result_fields:
            result[j] = row[j]
        for v in result.values():
            result_lst.append(v)
        writer.writerow(result_lst)