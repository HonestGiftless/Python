# takes_positive

def takes_positive(func):
    def wrapper(*args, **kwargs):
        rst = [*args, *kwargs.values()]
        if all([True if isinstance(i, int) else False for i in rst]):
            if all([True if i > 0 else False for i in rst]):
                return func(*args, **kwargs)
            else:
                raise ValueError
        else:
            raise TypeError
        
    return wrapper

@takes_positive
def positive_sum(*args):
    return sum(args)
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))