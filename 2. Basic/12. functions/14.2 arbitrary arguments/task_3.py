# Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.

def mean(*args):
    if len(args) == 0:
        return 0.0
    else:
        total = 0
        counter = 0
        for i in args:
            if type(i) is int or type(i) is float:
                total += i
                counter += 1
        if counter != 0:
            return total / counter
        else:
            return 0.0