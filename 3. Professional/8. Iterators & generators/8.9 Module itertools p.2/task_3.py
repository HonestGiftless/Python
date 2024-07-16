# first_true()

def first_true(iterable, predicate):
    result = filter(predicate, iterable)

    return next(result, None)