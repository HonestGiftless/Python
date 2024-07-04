# ignore_exception
# Декоратор для обработки типов исключений

import functools

def ignore_exception(*arguments):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except arguments as err:
                print(f"Исключение {type(err).__name__} обработано")
        return wrapper
    return decorator

@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x
    
f(0)