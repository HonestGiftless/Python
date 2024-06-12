# IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.

import random

def generate_ip():
    ip = ''
    for i in range(4):
        element = random.randint(0, 255)
        if i != 3:
            ip += str(element) + '.'
        else:
            ip += str(element)
    return ip