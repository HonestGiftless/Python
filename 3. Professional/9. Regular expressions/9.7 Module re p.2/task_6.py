# abbreviate()
import re

def abbreviate(phrase: str) -> str:
    '''Функция принимает фразу и возвращает ее аббревиатуру.
    Функция принимает phrase (str) - фраза и возвращает str - аббревиатуру.'''
    result = re.findall(r'\b\w|[A-Z]', phrase)
    return "".join([i.upper() for i in result])