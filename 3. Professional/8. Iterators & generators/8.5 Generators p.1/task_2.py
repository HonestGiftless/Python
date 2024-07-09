# alternating_sequence()

def alternating_sequence(count=None):
    '''Функция для возвращения последовательности с очередностью положительных и отрицательных чисел.
    Функция принимает count (размер последовательности).'''
    value = 1
    if count == None:
        while True:
            if value % 2 == 0:
                yield -value
            else:
                yield value
            value += 1
    else:
        for i in range(1, count+1):
            if i % 2 == 0:
                yield -i
            else:
                yield i