# Правильный многоугольник

from math import tan, pi

n = float(input())
a = float(input())

s = (n * a ** 2) / (4 * tan(pi / n))
print(s)