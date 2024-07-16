# tabulate()

import itertools as it

def tabulate(func):
    for i in it.count():
        yield func(i+1)