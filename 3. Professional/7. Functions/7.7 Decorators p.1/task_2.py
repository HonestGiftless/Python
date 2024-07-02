# New print

old_print = print

def main(func):
    def wrapper(*args, **kwargs):
        args = [i.upper() if isinstance(i, str) else i for i in args ]

        if 'sep' in kwargs:
            kwargs['sep'] = kwargs['sep'].upper()
        else:
            kwargs['sep'] = " "

        if 'end' in kwargs:
            kwargs['end'] = kwargs['end'].upper()
        else:
            kwargs['end'] = "\n"

        old_print(*args, sep=kwargs.get('sep'), end=kwargs.get('end'))
    return wrapper

@main
def print(*args, **kwargs):
    return args, kwargs

print('hi', 'there', end='!')