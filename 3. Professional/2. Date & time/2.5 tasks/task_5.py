# Employees of the organization 😄

from datetime import datetime, timedelta

worker = dict()

for i in range(int(input())):
    data = input()
    worker[data[:-10].rstrip()] = datetime.strptime(data[-10:], '%d.%m.%Y')

counter = 0

for k, v in worker.items():
    if v == min(worker.values()):
        counter += 1

if counter > 1:
    for v in worker.values():
        if v == min(worker.values()):
            print(datetime.strftime(v, '%d.%m.%Y'), counter)
            break
else:
    for k, v in worker.items():
        if v == min(worker.values()):
            print(datetime.strftime(v, '%d.%m.%Y'), k)
            break