# Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через разделитель (sep). Если разделитель не задан, им служит пробел.

def concat(*args, sep=' '):
    result = ''
    if len(args) > 1:
        for i in range(len(args)):
            if i == 0:
                result += str(args[i]) + sep
            elif i == len(args) - 1:
                result += str(args[i])
            else:
                result += str(args[i]) + sep
    else:
        result = args[0]
    
    return result