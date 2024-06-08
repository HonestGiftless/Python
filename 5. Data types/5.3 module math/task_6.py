# Квадратное уравнение 🌶️🌶️

from math import *

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c

if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))