# Заполнение 2

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

rows, cols = input().split()
rows = int(rows)
cols = int(cols)
matrix = []

for i in range(cols):
    for j in range(1, rows + 1):
        x = [i for i in range(j, (rows*cols) + 1, rows)]
        if x not in matrix:
            matrix.append(x)
            x = []

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()