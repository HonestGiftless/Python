# След матрицы

size = int(input())
matrix = list()

for row in range(size):
    r = [int(i) for i in input().split()]
    if len(r) == size:
        matrix.append(r)
    else:
        print('Incorrect matrix size')

total = 0

for r in range(size):
    total += matrix[r][r]

print(total)