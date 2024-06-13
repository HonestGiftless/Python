# Функция index_of_nearest()

def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        result = list()
        minimal = 100000000000000000000
        for i in numbers:
            if abs(number - i) < minimal:
                result.append(abs(number - i))
        min_od = min(result)
        return result.index(min_od)