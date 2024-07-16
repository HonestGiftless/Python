# factorials()

import itertools as it
import operator

def factorials(n):
    return it.accumulate(range(1, n + 1), operator.mul)