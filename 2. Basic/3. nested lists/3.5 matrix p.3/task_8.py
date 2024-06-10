# Заполнение змейкой

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

for r in range(rows): # 0 1 2 3 4
    elem = []
    for c in range(cols): # 0 1 2 3 4
        if r == 0:
            for i in range(1, cols + 1):
                elem.append(i)
        else:
            if r % 2 != 0:
                for i in range(matrix[r-1][-1]+1, matrix[r-1][-1]+cols+1):
                    elem.append(i)
                elem = elem[::-1]
            else:
                for i in range(matrix[r-1][-1]+1, matrix[r-1][-1]+cols+1):
                    elem.append(i)
    matrix.append(elem)

                
for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()