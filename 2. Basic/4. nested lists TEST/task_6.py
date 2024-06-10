#  Латинский квадрат 🌶️

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
matrixCopy = []
total = 0

appendMatrixOneSize(matrix, size)

for r in range(size):
    el = []
    for c in range(size):
        el.append(matrix[c][r])
    matrixCopy.append(el)
    
for r in range(size):
    for c in range(1, size + 1):
        if c in matrix[r] and c in matrixCopy[r]:
            total += 1
            
if total == size*size:
    print('YES')
else:
    print('NO')