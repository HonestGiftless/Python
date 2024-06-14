# Sorting by column

import csv

with open('deniro.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=',', quotechar='"')
    needed_column = int(input())
    sorted_rows = sorted(rows, key=lambda item: int(item[needed_column - 1]) if needed_column == 3 else item[needed_column - 1])

    for row in sorted_rows:
        print(",".join(row))