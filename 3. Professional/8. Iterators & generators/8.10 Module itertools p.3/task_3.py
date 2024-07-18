# max_pair()

from itertools import pairwise

def max_pair(iterable):
    return sum(max(pairwise(iterable), key=sum))