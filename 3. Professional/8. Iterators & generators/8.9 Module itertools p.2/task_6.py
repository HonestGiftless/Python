# first_largest()

def first_largest(iterable, number):
    for index, value in enumerate(iterable):
        if value > number:
            return index

    return -1