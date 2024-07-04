# returns
# Декоратор для проверки типа данных

import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, datatype):
                return value
            else:
                raise TypeError
        return wrapper
    return decorator

@returns(int)
def add(a, b):
    return a + b

print(add(10, 5))