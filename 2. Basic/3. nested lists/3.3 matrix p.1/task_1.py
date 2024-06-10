# Вывести матрицу 1

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

rows, cols = int(input()), int(input())
matrix = []

for r in range(rows):
    elem = []
    for c in range(cols):
        elem.append(input())
    matrix.append(elem)
    elem = []
    
printMatrixAnySize(matrix, rows, cols)