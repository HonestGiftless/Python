# Математические функции

import math

def get_square(num):
    return num**2

def get_cube(num):
    return num**3

def get_square_root(num):
    return num**(1/2)

def get_absolute(num):
    return abs(num)

def get_angle(num):
    return math.sin(num)

functions = {'квадрат': get_square,
             'куб': get_cube,
             'корень': get_square_root,
             'модуль': get_absolute,
             'синус': get_angle}

number = int(input())
function = input().lower()

print(functions[function](number))