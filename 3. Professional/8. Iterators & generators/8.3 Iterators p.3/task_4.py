# random_numbers()

from random import choice

def random_numbers(left: int, right: int) -> iter:
    '''Функция принимает:
    left - целое число, левая граница диапазона
    right - целое число, правая граница диапазона.
    Возвращает бесконечный итератор в диапазоне от left до right.'''
    return iter(lambda: choice(list(range(left, right+1))), '')

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))