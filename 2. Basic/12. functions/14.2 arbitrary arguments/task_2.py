# Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.

def sq_sum(*args):
    total = 0
    for i in args:
        total += i**2
    return total