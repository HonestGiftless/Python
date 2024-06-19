# Бесплатные курсы берут свое 😢

import csv
import json
from collections import Counter

def csv_file_opens(filenames):
    result = list()

    for filename in filenames:
        with open(filename, encoding='utf-8') as file:
            lst = list(csv.reader(file))
            lst = lst[1:]
        result.append(lst)

    return result

counter = Counter()
all_data = csv_file_opens(['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv'])

for data in all_data:
    for product in data:
        counter[product[0]] += sum(list(map(int, product[1:])))

result_prices = Counter()

with open('prices.json', encoding='utf-8') as json_file:
    result = json.load(json_file)
    for k, v in result.items():
        result_prices[k] += v * counter[k]

print(result_prices.total())