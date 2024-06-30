# numbers_sum()

def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda item: isinstance(item, int) or isinstance(item, float), elems))