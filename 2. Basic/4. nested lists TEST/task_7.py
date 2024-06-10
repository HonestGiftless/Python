# Ходы ферзя

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
        
size = 8
matrix = []
listSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pos = input()

for r in range(size):
    el = ['.'] * 8
    matrix.append(el)
    
symbPos = listSymbols.index(pos[0])
numPos = int(pos[1])
matrix[-numPos][symbPos] = 'Q'

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'Q':
            indexCol = matrix[r].index(matrix[r][c])
            for i in range(indexCol):
                matrix[r][i] = '*' 
            for i in range(indexCol+1, size):
                matrix[r][i] = '*'
        if c == symbPos:
            matrix[r][c] = '*'
            
matrix[-numPos][symbPos] = 'Q'

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'Q':
            for i in range(r-1, -1, -1):
                for j in range(c+1, size):
                    for x in range(1, size):
                        if r - i == x and j - c == x:
                            matrix[i][j] = '*'
            for i in range(r+1, size):
                for j in range(c+1, size):
                    for x in range(1, size):
                        if i - r == x and j - c == x:
                            matrix[i][j] = '*'
            for i in range(r-1, -1, -1):
                for j in range(c-1, -1, -1):
                    for x in range(c, 0, -1):
                        if r - i == x and c - j == x:
                            matrix[i][j] = '*'
            for i in range(r+1, size):
                for j in range(c-1, -1, -1):
                    for x in range(c, 0, -1):
                        if i - r == x and c - j == x:
                            matrix[i][j] = '*'
            
printMatrixOneSize(matrix, size)