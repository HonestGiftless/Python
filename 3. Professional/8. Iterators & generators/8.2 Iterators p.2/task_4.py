# starmap()

def starmap(func, iterable):
    '''Функция для применения map во вложенных коллекциях.'''
    result = map(func, *zip(*iterable))

    return result