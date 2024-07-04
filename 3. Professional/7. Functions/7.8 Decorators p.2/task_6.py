# repeat
# Декоратор для вызова функции times раз

import functools

def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
                for i in range(times - 1):
                    func(*args, **kwargs)
                return func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
say_beegeek()