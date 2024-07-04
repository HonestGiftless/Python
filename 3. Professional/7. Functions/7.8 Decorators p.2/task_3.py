# trace
# Декоратор для вывода отладочной информации о функции

import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        value = func(*args, **kwargs)
        if isinstance(value, str):
            print(f"TRACE: возвращаемое значение {func.__name__}(): '{value}'")
        else:
            print(f"TRACE: возвращаемое значение {func.__name__}(): {value}")
        return value
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'
    
say('Jane', 'Hello, World')