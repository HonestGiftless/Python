# Employees of the organization 😔

from datetime import datetime, timedelta

current_date = datetime.strptime(input(), '%d.%m.%Y')
maximal_date = current_date + timedelta(days=7)

worker = dict()

for i in range(int(input())):
    data = input()
    worker[data[:-10].rstrip()] = datetime.strptime(data[-10:], '%d.%m.%Y')

done_worker = dict()

for k, v in worker.items():
    if current_date < datetime(year=maximal_date.year, month=v.month, day=v.day) <= maximal_date:
        done_worker[k] = v

if len(done_worker) != 0:
    minimal = max(done_worker.values())

    for k, v in done_worker.items():
        if v == minimal:
            print(k)
else:
    print("Дни рождения не планируются")