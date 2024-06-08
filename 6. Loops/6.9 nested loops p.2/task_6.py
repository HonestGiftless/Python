# Сумма факториалов

from math import factorial

num = int(input())
total = 0

for i in range(1, num + 1):
    total += factorial(i)

print(total)