# Обмен столбцов

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

rows, cols = int(input()), int(input())
matrix = []

for r in range(rows):
    elem = [int(i) for i in input().split()]
    if len(elem) == cols:
        matrix.append(elem)

changes = [int(i) for i in input().split()]

for r in range(rows):
    matrix[r][changes[0]], matrix[r][changes[1]] = matrix[r][changes[1]], matrix[r][changes[0]]

printMatrixAnySize(matrix, rows, cols)