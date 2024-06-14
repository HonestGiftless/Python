# Panoramic Agency

import sys

data = [i.strip('\n') for i in sys.stdin]

for i in range(len(data)):
    if "/" in data[i]:
        data[i] = data[i].split(" / ")

for i in data:
    if "." in i[-1]:
        i[-1] = float(i[-1])

dct = dict()

for i in data:
    if i[-2] == data[-1]:
        dct[i[0]] = i[-1]

result = list()

for k, v in dct.items():
    result.append((k, v))

result = list(sorted(result, key=lambda x: (x[1], x[0])))

for i in result:
    print(i[0])