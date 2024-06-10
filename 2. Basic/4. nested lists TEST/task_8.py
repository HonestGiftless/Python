# Диагонали, параллельные главной

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
        
size =  int(input())
matrix = []

for i in range(size):
    matrix.append(['.']*size)
    
for i in range(size):
    for j in range(size):
        if i == j:
            matrix[i][j] = 0
        for x in range(1, size):
            if i - j == x:
                matrix[i][j] = x
            if j - i == x:
                matrix[i][j] = x

printMatrixOneSize(matrix, size)