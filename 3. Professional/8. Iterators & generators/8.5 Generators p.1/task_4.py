# reverse()

def reverse(sequence):
    '''Функция для изменения порядка последовательности.
    Функция принимает sequence (исходная последовательность).'''
    for i in range(len(sequence) - 1, -1, -1):
        yield sequence[i]