# Голодный студент 🌶️

import csv

with open("prices.csv", 'r', encoding='utf-8', newline='') as file:
    rows = csv.DictReader(file, delimiter=";")
    fields = rows.fieldnames

    minimals = dict()

    for row in rows:
        valid_prices = {key: int(value) for key, value in row.items() if value.isdigit()}
        min_price_key = min(valid_prices, key=valid_prices.get)
        minimals[row["Магазин"]] = [min_price_key, valid_prices[min_price_key]]

    result = list()

    for k, v in minimals.items():
        result.append([k] + v)

    result = sorted(result, key=lambda item: (item[2], item[1]))
    print(result[0][1], result[0][0], sep=': ')