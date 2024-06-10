# Максимальный в области 1

size = int(input())
matrix = list()

for row in range(size):
    r = [int(i) for i in input().split()]
    if len(r) == size:
        matrix.append(r)
    else:
        print('Incorrect matrix size')

maximal = -1000000000000000000

for r in range(size):
    c = 0
    while c <= r:
        if matrix[r][c] > maximal:
            maximal = matrix[r][c]
        c += 1

print(maximal)