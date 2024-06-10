# Заполнение 1

def print_matrix(rows, cols, mtr):
    for r in range(rows):
        for c in range(cols):
            print(mtr[r][c], end=' ')
        print()

size = [int(i) for i in input().split()]
matrix = []
counter = 1

for r in range(size[0]):
    elem = []
    for c in range(size[1]):
        elem.append(counter)
        counter += 1
    matrix.append(elem)
    
print_matrix(size[0], size[1], matrix)