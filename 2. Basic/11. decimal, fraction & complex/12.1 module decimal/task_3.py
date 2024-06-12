# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

from decimal import *

num = Decimal(input())
num = str(num).split('.')
txt = ''

for i in num:
    txt += i.strip('-')

total = 0
maximum = -1
minimal = 10
for i in txt:
    if int(i) > maximum:
        maximum = int(i)
    if int(i) < minimal:
        minimal = int(i)

print(maximum + minimal)