# get_digits()

def get_digits(number: int | float) -> list[int]:
    '''Функция принимает число (целое, или вещественное)
    Возвращет список цифр этого числа'''
    return [int(i) for i in str(number) if i.isdigit()]