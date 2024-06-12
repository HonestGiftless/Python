# Сумма дробей 1

from fractions import Fraction

n = int(input())
total = 0

for i in range(1, n + 1):
    total += Fraction(f'1/{i**2}')
    
print(total)