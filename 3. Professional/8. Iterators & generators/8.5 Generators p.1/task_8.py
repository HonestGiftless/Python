# palindromes()

def palindromes(start=1):
    '''Функция для генерации последовательности чисел-палиндромов.'''
    while True:
        if str(start) == str(start)[::-1]:
            yield start
        start += 1