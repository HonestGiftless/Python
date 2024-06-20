# Zoo

import json
from collections import ChainMap

result = ChainMap()
total = 0

with open("zoo.json", encoding="utf-8") as file:
    rows = json.load(file)
    for row in rows:
        result.update(row)

for k, v in result.items():
    total += v

print(total)