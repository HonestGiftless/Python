# sum_of_digits()

from itertools import chain

def sum_of_digits(iterable):
    return sum((int(i) for i in chain.from_iterable(map(str, iterable))))