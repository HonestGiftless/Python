# unique()

from collections import Counter

def unique(iterable):
    return iter(Counter(iterable))