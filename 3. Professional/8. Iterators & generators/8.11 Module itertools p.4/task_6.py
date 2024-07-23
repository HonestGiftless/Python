# ranges() 🌶️

from itertools import groupby

def ranges(numbers: list):
    test = groupby(sorted(numbers, key=lambda x: numbers.index(x) - x), key=lambda x: numbers.index(x) - x)
    result = list()

    while True:
        try:
            item = next(test)
            number_range = list(item[1])
            result.insert(0, (number_range[0], number_range[-1]))
        except:
            break

    return result