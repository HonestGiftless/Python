# Сложение матриц

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

firstMatrix = []
for r in range(rows):
    elem = [int(i) for i in input().split()]
    if len(elem) == cols:
        firstMatrix.append(elem)

emptyStr = input()

secondMatrix = []
for r in range(rows):
    elem = [int(i) for i in input().split()]
    secondMatrix.append(elem)

cMatrix = []

for r in range(rows):
    elem = []
    for c in range(cols):
        elem.append(firstMatrix[r][c] + secondMatrix[r][c])
    cMatrix.append(elem)

printMatrixAnySize(cMatrix, rows, cols)