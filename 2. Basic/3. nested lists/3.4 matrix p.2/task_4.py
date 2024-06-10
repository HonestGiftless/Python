# Симметричная матрица

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
hasSim = False

appendMatrixOneSize(matrix, size)

for r in range(size):
    for c in range(size):
        if matrix[r][c] == matrix[c][r]:
            total += 1

if total == size * size:
    hasSim = True

if hasSim:
    print('YES')
else:
    print('NO')