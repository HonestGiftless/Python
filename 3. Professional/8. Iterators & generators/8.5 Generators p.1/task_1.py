# simple_sequence()

def simple_sequence():
    '''Функция для возвращения последовательности натуральных чисел, состоящее из такого количества каждого числа, каково оно.'''
    value = 1
    while True:
        for _ in range(value):
            yield value
        value += 1