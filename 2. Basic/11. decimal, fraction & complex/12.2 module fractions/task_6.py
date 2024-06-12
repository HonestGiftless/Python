# Сумма дробей 2

from fractions import Fraction
from math import factorial

n = int(input())
total = 0

for i in range(1, n + 1):
    total += Fraction(1, factorial(i))
    
print(total)