# intersperse

def intersperse(iterable, delimiter):
    result = list()
    for i in iterable:
        result.append(i)
        result.append(delimiter)
    result = iter(result[:-1])
    for i in result:
        yield i