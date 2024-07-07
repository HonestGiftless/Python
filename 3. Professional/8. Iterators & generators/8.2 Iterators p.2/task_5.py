# get_min_max() 😳

def get_min_max(iterable) -> tuple:
    '''Функция принимает итерируемый объект.
    Возвращает кортеж из минимального и максимального элемента.'''
    iterable = iter(iterable)
    try:
        start = next(iterable)
    except StopIteration:
        return None
    
    minimum, maximum = start, start
    
    while True:
        try:
            current = next(iterable)
            if current > maximum:
                maximum = current
            if current < minimum:
                minimum = current
        except:
            break
    
    return (minimum, maximum)