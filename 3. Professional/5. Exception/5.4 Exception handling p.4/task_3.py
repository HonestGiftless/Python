# Deserialization

import json

filename = input()

try:
    with open(filename, encoding='utf-8') as json_file:
        try:
            rows = json.load(json_file)
        except json.JSONDecodeError:
            print("Ошибка при десериализации")
        else:
            print(rows)
except OSError:
    print("Файл не найден")