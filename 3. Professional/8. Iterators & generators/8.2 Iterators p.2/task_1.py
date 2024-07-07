# filterfalse()

def filterfalse(predicate, iterable: iter) -> iter:
    '''Функция работает противоположно функции filter.
    Возвращает все значения, у которых filter вернула False.'''
    if predicate is None:
        predicate = bool
    result = filter(lambda x: not predicate(x), iterable)
    return result