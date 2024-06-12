# Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и возвращает приветствие в соответствии с образцом.

def greet(name, *args):
    if len(args) == 0:
        return 'Hello, ' + str(name) + '!'
    else:
        txt = f'Hello, {str(name)} and'
        for i in range(len(args)):
            if len(args) == 1:
                txt += f' {args[i]}!'
            else:
                if i != len(args) - 1:
                    txt += f' {args[i]} and'
                else:
                    txt += f' {args[i]}!'
        return txt