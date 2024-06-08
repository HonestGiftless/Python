# Площадь и длина

from math import pi

def get_circle(radius):
    length = 2 * pi * radius
    square = pi * r**2

    return length, square

r = float(input())

length, square = get_circle(r)
print(length, square)