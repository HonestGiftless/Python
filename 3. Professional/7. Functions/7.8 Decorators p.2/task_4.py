# prefix
# Декоратор для добавления символа в строку (в начало или конец)

import functools

def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return str(func(*args, **kwargs)) + string
            else:
                return string + str(func(*args, **kwargs))
        return wrapper
    return decorator

@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())