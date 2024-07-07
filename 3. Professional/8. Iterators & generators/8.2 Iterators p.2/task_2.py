# transpose()

def transpose(matrix: list[list]) -> list:
    '''Функция транспонирования матрицы.
    Принимает на вход вложенный список.
    Возвращает вложенный список.'''
    result = [list(row) for row in zip(*matrix, strict=True)]
    return result