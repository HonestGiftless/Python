# Шахматная доска

def print_matrix(rows, cols, mtr):
    for r in range(rows):
        for c in range(cols):
            print(mtr[r][c], end=' ')
        print()

size = [int(i) for i in input().split()]
matrix = []

for r in range(size[0]):
    elem = []
    for c in range(size[1]):
        if (r % 2 == 0 and c % 2 == 0) or (r % 2 != 0 and c % 2 != 0):
            elem.append('.')
        elif (r % 2 == 0 and c % 2 != 0) or (r % 2 != 0 and c % 2 == 0):
            elem.append('*')
    matrix.append(elem)

print_matrix(size[0], size[1], matrix)