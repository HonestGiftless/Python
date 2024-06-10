# Заполнение диагоналями 🌶️

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

n, m = [int(i) for i in input().split()]
mtx = [[0] * m for _ in range(n)]
sequence, k = 1, 0

while sequence != n * m + 1:
    for i in range(n):
        for j in range(m):
            if i + j == k:
                mtx[i][j] = sequence
                sequence += 1
    k += 1

printMatrixAnySize(mtx, n, m)