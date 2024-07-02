# exception_decorator

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        result = tuple()
        try:
            result = (func(*args, **kwargs), 'Функция выполнилась без ошибок')
        except:
            result = (None, 'При вызове функции произошла ошибка')
        
        return result
    
    return wrapper

@exception_decorator
def f(x):
    return x**2 + 2*x + 1
    
print(f(7))