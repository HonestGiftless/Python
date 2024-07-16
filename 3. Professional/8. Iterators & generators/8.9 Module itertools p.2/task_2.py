# drop_this()

from itertools import dropwhile, takewhile, filterfalse, compress

def drop_this(iterable, obj):
    return dropwhile(lambda item: item == obj, iterable)