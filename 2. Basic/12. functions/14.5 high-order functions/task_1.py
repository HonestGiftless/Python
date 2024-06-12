# Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 
# 2 десятичных знаков, а затем выводит их, каждый на отдельной строке.

def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def reduce(operation, items, initial_values):
    acc = initial_values
    for item in items:
        acc = operation(acc, item)
    return acc

def shorten(num):
    return round(num, 2)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
new_numbers = map(shorten, numbers)

print(*new_numbers, sep='\n')