# Тригонометрическое выражение

from math import *

x = float(input())
x_rad = radians(x)

sin_x = sin(x_rad)
cos_x = cos(x_rad)
tan_x = pow(tan(x_rad), 2)

print(sin_x + cos_x + tan_x)