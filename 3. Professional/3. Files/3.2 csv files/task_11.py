# Проще, чем кажется 🌶️

import csv

def condense_csv(filename, id_name):
    fields = [id_name]
    result = list()
    result_dict = dict()
    rst = list()

    with open(filename, 'r', encoding='utf-8', newline='') as file:
        rows = csv.reader(file, delimiter=',')

        for row in rows:
            elem = list()

            for j in range(1, len(row), 2):
                if row[j] not in fields:
                    fields.append(row[j])

            for j in range(len(row)):
                if row[j] not in fields:
                    elem.append(row[j])

            result.append(elem)
        
        for i in result:
            if i[0] not in result_dict.keys():
                result_dict[i[0]] = [i[1]]
            else:
                result_dict[i[0]] += [i[1]]

        for k, v in result_dict.items():
            element = [k]
            for i in v:
                element.append(i)
            rst.append(element)

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(rst)