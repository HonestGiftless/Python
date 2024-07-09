# primes()

def primes(left: int, right: int):
    '''Функция для создания последовательности простых чисел.
    Функция принимает left (начальное число последовательности) и right (конечное число последовательности).'''
    def is_prime(num):
        has_div = False

        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    has_div = True
                    break
        else:
            has_div = True
        
        return has_div

    for num in range(left, right + 1):
        if not is_prime(num):
            yield num