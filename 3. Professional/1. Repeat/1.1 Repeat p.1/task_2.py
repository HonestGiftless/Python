# Функция same_parity()

def same_parity(numbers):
    result = list()

    for num in numbers:
        if num % 2 == numbers[0] % 2:
            result.append(num)

    return result