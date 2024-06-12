# Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 
# 1 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).

import random

numbers = [i for i in range(1, 76)]
matrix = []

while len(matrix) != 5:
    elem = set()
    while len(elem) != 5:
        x = random.choice(numbers)
        elem.add(x)
        numbers.remove(x)
    if elem not in matrix:
        elem = list(elem)
        matrix.append(elem)
    else:
        continue

matrix[2][2] = 0

for r in range(5):
    for c in range(5):
        print(str(matrix[r][c]).ljust(3), end='')
    print()