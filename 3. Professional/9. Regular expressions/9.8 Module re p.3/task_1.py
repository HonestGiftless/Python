# normalize_jpeg()
import re

def normalize_jpeg(filename: str) -> str:
    '''Функция принимает имя файла (str) с форматом jpeg или jpg (в произвольном регистре)
    Функция возвращает имя файла с нормализованным расширением jpg (str)'''
    return re.sub(r'jpg$|jpeg$', r'jpg', filename, flags=re.IGNORECASE)