# normalize_whitespace()
import re

def normalize_whitespace(string: str) -> str:
    '''Функция принимает произвольную строку (str).
    Возвращет строку без множественных пробелов.'''
    return re.sub(r'\s{2,}', r' ', string)