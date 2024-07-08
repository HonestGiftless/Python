# is_iterable()

def is_iterable(obj) -> bool:
    '''Функция принимает любой объект и проверяет, является ли он итерируемым объектом.
    Возвращаемые значения: True или False.'''
    try:
        iter(obj)
        return True
    except:
        return False

print(is_iterable(18731))