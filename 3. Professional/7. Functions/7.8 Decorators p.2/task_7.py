# strip_range
# Декоратор для замены символов

import functools

def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if end < len(func(*args, **kwargs)):
                value = func(*args, **kwargs)[:start] + (char * (end - start)) + func(*args, **kwargs)[end:]
            else:
                value = func(*args, **kwargs)[:start]
                while len(value) != len(func(*args, **kwargs)):
                    value += char
            return value
        return wrapper
    return decorator

@strip_range(3, 5)
def beegeek():
    return 'beegeek'
    
print(beegeek())