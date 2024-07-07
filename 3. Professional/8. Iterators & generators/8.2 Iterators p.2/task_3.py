# get_min_max()

def get_min_max(data: list) -> tuple:
    '''Функция принимает на вход список.
    Возвращает кортеж из индексов минимального и максимального элемента.'''
    result = list(enumerate(data))

    if data:
        return (min(result, key=lambda item: item[1])[0], max(result, key=lambda item: item[1])[0])