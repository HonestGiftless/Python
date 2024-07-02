# reverse_args

def reverse_args(func):
    def wrapper(*args, **kwargs):
        result = list(kwargs.values())[::-1] + list(args[::-1])

        return func(*result)

    return wrapper

@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))