# Максимум в таблице

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
maximal = -1000000
mostBiggestFinded = False

for r in range(rows):
    elem = [int(i) for i in input().split()]
    if len(elem) == cols:
        matrix.append(elem)

maxElem = max(max(matrix, key=max))

for r in range(rows):
    if mostBiggestFinded == False:
        for c in range(cols):
            if matrix[r][c] == maxElem:
                print(r, c)
                mostBiggestFinded = True
                break;
    else:
        break