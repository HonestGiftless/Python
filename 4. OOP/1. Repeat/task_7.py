# quantify

def quantify(iterable, predicate) -> int:
    if predicate is None:
        predicate = bool
    result = filter(lambda x: predicate(x), iterable)
    return len(list(result))