# ncycles()

from itertools import chain, tee

def ncycles(iterable, times):
    return chain(*tee(iterable, times))