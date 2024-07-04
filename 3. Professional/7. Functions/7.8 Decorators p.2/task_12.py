# retry
# Декоратор для попыток вызова функции и возбуждения пользовательского исключения истечения попыток

import functools

class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    continue
            raise MaxRetriesException
        return wrapper
    return decorator

@retry(3)
def no_way():
    raise ValueError
   
try:
    no_way()
except Exception as e:
    print(type(e))