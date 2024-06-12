# Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

from functools import reduce

def product_of_odds(data):
    x = reduce(lambda x, y: x*y, filter(lambda z: z % 2 == 1, data), 1)
    return x