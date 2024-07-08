# is_iterator()

def is_iterator(obj) -> bool:
    '''Функция принимает любой объект и проверяет, является ли он итератором.
    Возвращаемые значения: True или False.'''
    return '__next__' in dir(obj)

print(is_iterator([1, 2, 3, 4, 5]))