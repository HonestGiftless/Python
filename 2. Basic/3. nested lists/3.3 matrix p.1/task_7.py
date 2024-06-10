# Суммы четвертей

def printMatrixOneSize(mtrx, size):
    for r in range(size):
        for c in range(size):
            print(mtrx[r][c], end=' ')
        print()
        
def printMatrixAnySize(mtrx, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(mtrx[r][c], end=' ')
        print()
        
def appendMatrixOneSize(mtrx, size):
    for _ in range(size):
        elem = [int(i) for i in input().split()]
        mtrx.append(elem)
        
def appendMatrixAnySize(mtrx, rows, cols):
    for r in range(rows):
        elem = []
        for c in range(cols):
            elem.append(input())
        mtrx.append(elem)

size = int(input())
matrix = []
total = 0

appendMatrixOneSize(matrix, size)

# Верхняя
for r in range(size):
    for c in range(size):
        if r < c and r < size-1-c:
            total += matrix[r][c]

print('Верхняя четверть:', total)
total = 0

# Правая
for r in range(size):
    for c in range(size):
        if r < c and r > size-1-c:
            total += matrix[r][c]

print('Правая четверть:', total)
total = 0

# Нижняя
for r in range(size):
    for c in range(size):
        if r > c and r > size-1-c:
            total += matrix[r][c]

print('Нижняя четверть:', total)
total = 0

# Левая
for r in range(size):
    for c in range(size):
        if r > c and r < size-1-c:
            total += matrix[r][c]

print('Левая четверть:', total)