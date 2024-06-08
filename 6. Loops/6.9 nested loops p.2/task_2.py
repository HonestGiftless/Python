# Численный треугольник 3

num = int(input())

for row in range(1, num + 1):
    for col in range(1, row):
        print(col, sep='', end='')
    for col in range(row, 0, -1):
        print(col, sep='', end='')
    print()