# Таблица умножения

def printMatrixOneSize(mtrx, size):
    for r in range(size):
        for c in range(size):
            print(mtrx[r][c], end=' ')
        print()
        
def printMatrixAnySize(mtrx, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(3), end=' ')
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
    elem = []
    for c in range(cols):
        if r == 0:
            elem.append(0)
        else:
            if c == 0 and r != 0:
                elem.append(0)
            else:
                if r == 1 and c != 0:
                    for i in range(1, cols):
                        elem.append(i)
                else:
                    if r == 2 and c == 1:
                        elem.append(2)
                    else:
                        elem.append(r * c)
    matrix.append(elem)

printMatrixAnySize(matrix, rows, cols)