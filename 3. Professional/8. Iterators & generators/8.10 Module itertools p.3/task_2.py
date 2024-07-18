# is_rising()

from itertools import chain, zip_longest, tee, pairwise

def is_rising(iterable):
    pairs = pairwise(iterable)
    return all(True if i[0] < i[1] else False for i in pairs)