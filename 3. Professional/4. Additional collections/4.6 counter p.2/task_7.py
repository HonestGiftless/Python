# Here we go again

import csv
from collections import Counter

with open("name_log.csv", encoding='utf-8') as file:
    rows = list(row[1] for row in csv.reader(file))[1:]
    counter = sorted(Counter(rows).items(), key=lambda item: item[0])

    for email in counter:
        print(f"{email[0]}: {email[1]}")