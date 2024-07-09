# flatten()

def flatten(nested_list):
    '''Рекурсивная функция для получения числовых значений из списков любой вложенности.
    Функция принимает nested_list (вложенный список).'''
    for item in nested_list:
        if isinstance(item, int):
            yield item
        else:
            yield from flatten(item)