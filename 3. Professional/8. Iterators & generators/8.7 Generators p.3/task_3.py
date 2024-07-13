# filter_names()

def filter_names(names: list, ignore_char: str, max_names: int):
    '''Функция для фильтрации имен.
    Функция принимает в себя names - list
    ignore_char - str
    max_names - int.'''
    
    if max_names > len(names):
        max_names = len(names)

    without_digits = (name for name in names if name.isalpha() and not name.lower().startswith(ignore_char.lower()))

    for index, num in enumerate(without_digits):
        if index < max_names:
            yield num