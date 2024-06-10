# Вывести матрицу 2

rows, cols = int(input()), int(input())
matrix = list()

for row in range(rows):
    r = list()
    for col in range(cols):
        elem = input()
        r.append(elem)
    matrix.append(r)

for row in range(rows):
    for col in range(cols):
        print(matrix[row][col], end=' ')
    print()

print()

for col in range(cols):
    for row in range(rows):
        print(matrix[row][col], end=' ')
    print()