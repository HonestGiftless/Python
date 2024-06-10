# Больше среднего

size = int(input())
matrix = list()

for row in range(size):
    r = [int(i) for i in input().split()]
    if len(r) == size:
        matrix.append(r)
    else:
        print('Incorrect matrix size')

more_than_average = list()

for row in range(size):
    average = sum(matrix[row]) / len(matrix[row])
    counter = 0
    for col in range(size):
        if matrix[row][col] > average:
            counter += 1
    more_than_average.append(counter)

print(*more_than_average, sep='\n')