# add_attrs
# Декоратор для добавления пользовательских атрибутов функции

import functools

def add_attrs(**kwarguments):
    def decorator(func):
        for k in kwarguments:
            func.__dict__[k] = kwarguments[k]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)