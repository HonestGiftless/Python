# drop_while_negative()

from itertools import dropwhile, takewhile, filterfalse, compress

def drop_while_negative(iterable):
    return dropwhile(lambda item: item < 0, iterable)