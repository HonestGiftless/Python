# Sorted dates

from datetime import date

n = int(input())
dates = list()

for i in range(n):
    dates.append(date.fromisoformat(input()))

x = sorted(dates)

for i in x:
    print(i.strftime('%d/%m/%Y'))