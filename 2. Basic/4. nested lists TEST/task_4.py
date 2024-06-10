# Снежинка

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

for r in range(size):
    elem = []
    for c in range(size):
        elem.append('.')
    matrix.append(elem)
    
for r in range(size):
    matrix[r][r] = '*'
    matrix[r][size-r-1] = '*'
    
for r in range(size):
    for c in range(size):
        if size % 2 != 0:
            if c == size // 2 or r == size // 2:
                matrix[r][c] = '*'

printMatrixOneSize(matrix, size)