# Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список, в котором каждое значение будет результатом применения переданной функции к переданному списку.

def func_apply(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result