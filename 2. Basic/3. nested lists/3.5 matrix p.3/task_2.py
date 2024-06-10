# Побочная диагональ

def print_matrix(n, mtr):
    for r in range(n):
        for c in range(n):
            print(mtr[r][c], end=' ')
        print()

n = int(input())
matrix = []

for i in range(n):
    elem = []
    for j in range(n):
        elem.append(0)
    matrix.append(elem)

for i in range(n):
    matrix[i][n-i-1] = 1
    for j in range(n):
        if (i < j and i > n - 1 - j) or (i >= j and i > n - 1 - j):
            matrix[i][j] = 2
            

print_matrix(n, matrix)