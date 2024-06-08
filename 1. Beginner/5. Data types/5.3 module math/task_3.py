# Средние значения

from math import *

a = float(input())
b = float(input())

aver_ar = (a+b)/2
aver_g = sqrt(a*b)
aver_gar = (2 * a * b) / (a + b)
aver_sq = sqrt((a**2 + b**2) / 2)

print(aver_ar, '\n', aver_g, '\n', aver_gar, '\n', aver_sq, sep='')