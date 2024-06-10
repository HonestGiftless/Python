# Заполнение спиралью 😈😈

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
mat = [[0] * int(m) for i in range(n)]

c = 1        
a, b = 0, 0
rows = n - 1
cols = m - 1

while a <= cols and b <= rows:
    for i in range(a, cols + 1):
        mat[a][i] = c
        c += 1
    b += 1
    for i in range(b, rows + 1):
        mat[i][cols] = c
        c += 1
    cols -= 1
    if b <= rows:
        for i in range(cols, a-1, -1):
            mat[rows][i] = c
            c += 1
        rows -= 1
    if a <= cols:
        for i in range(rows, b-1, -1):
            mat[i][a] = c
            c += 1
        a += 1

for s in mat:
    print(*s)