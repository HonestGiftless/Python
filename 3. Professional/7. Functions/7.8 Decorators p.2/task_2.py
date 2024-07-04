# returns_string
# Декоратор для возвращения только строк

import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if all([True if isinstance(i, str) else False for i in args]) and all([True if isinstance(i, str) else False for i in kwargs.values()]):
            if func(*args, **kwargs) != None:
                return func(*args, **kwargs)
            else:
                raise TypeError
        else:
            raise TypeError
    return wrapper

@returns_string
def beegeek():
    return 'beegeek'
    
print(beegeek())