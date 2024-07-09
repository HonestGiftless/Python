# dates()

from datetime import date, timedelta

def dates(start, count=None):
    '''Функция для создания последовательности дат.
    Функция принимает start (начальная дата).
    Функция принимает необязательный параметр count (количество дат).
    Функция возвращает последовательность всех дат от начальной до максимальной (9999-12-31) в обычном случае.'''
    if count == None:
        needed_date = date.max
    else:
        needed_date = start + timedelta(days=count-1)
            
    while start < needed_date:
        yield start
        start += timedelta(days=1)

    if start == needed_date:
        yield start
    else:
        return StopIteration