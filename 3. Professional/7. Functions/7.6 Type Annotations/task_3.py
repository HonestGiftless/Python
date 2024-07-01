# cyclic_shift()

def cyclic_shift(numbers: list[int | float], step: int) -> None:
    '''Функция принимает список чисел (целые или вещественные) и шаг смещения (целое число)
    Ничего не возвращает, а изменяет исходный список, смещяя элементы'''
    result = numbers

    if step > 0:
        for i in range(step):
            item = result[-1]
            del result[-1]
            result.insert(0, item)
    else:
        for i in range(abs(step)):
            item = result[0]
            del result[0]
            result.append(item)