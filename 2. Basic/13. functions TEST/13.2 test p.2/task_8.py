# Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции.

def arithmetic_operation(action):
     return {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}[action]