# Заполнение 5 🌶️

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

for r in range(rows):
    elem = []
    for c in range(cols):
        elem.append((r+c)%cols+1)
    matrix.append(elem)
    
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()