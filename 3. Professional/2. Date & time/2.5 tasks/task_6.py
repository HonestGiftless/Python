# Employees of the organization 🙂

from datetime import datetime

worker = dict()
counter = dict()

for i in range(int(input())):
    data = input()
    worker[data[:-10].rstrip()] = datetime.strptime(data[-10:], '%d.%m.%Y')

for k, v in worker.items():
    if v not in counter:
        counter[v] = 1
    else:
        counter[v] += 1

result = list()

for k, v in counter.items():
    if v == max(counter.values()):
        if k not in result:
            result.append(k)

result = sorted(result)

for dat in result:
    print(datetime.strftime(dat, '%d.%m.%Y'))