# Функция print_given()

def print_given(*args, **kwargs):
    if len(args) != 0:
        if len(kwargs) != 0:
            for i in args:
                print(i, type(i))
            kwargs = dict(sorted(kwargs.items()))
            for k, v in kwargs.items():
                print(k, v,  type(v))
        else:
            for i in args:
                print(i, type(i))
    else:
        if len(kwargs) != 0:
            kwargs = dict(sorted(kwargs.items()))
            for k, v in kwargs.items():
                print(k, v,  type(v))