# multiple_split()
import re

def multiple_split(string: str, delimiters: list) -> list:
    '''Функция принимает string (str) и delimiters (list).
    Возвращает список из строки, разделенной по символам из списка delimiters.'''
    items = '|'.join(map(re.escape, delimiters))
    return re.split(items, string)