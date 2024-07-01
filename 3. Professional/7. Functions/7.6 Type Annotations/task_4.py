# matrix_to_dict()

def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    '''Функция принимает матрицу (вложенные списки из чисел)
    Возвращает словарь, ключи - целые числа (номера строк), а значения - список (строка матрицы)'''
    return {r + 1: matrix[r] for r in range(len(matrix))}