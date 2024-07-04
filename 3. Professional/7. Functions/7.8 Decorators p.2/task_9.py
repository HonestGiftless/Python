# takes
# Декоратор для проверки соответствия аргументов к типу данных

import functools

def takes(*arguments):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not all([True if type(i) in arguments else False for i in args]):
                raise TypeError
            else:
                if len(kwargs) > 0 and not all([True if type(i) in arguments else False for i in kwargs.values()]):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))