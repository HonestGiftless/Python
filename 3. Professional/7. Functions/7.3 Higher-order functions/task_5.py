# print_operation_table()

def print_operation_table(operation, rows, cols):
    matrix = []
    for row in range(1, rows + 1):
        elem = []
        for col in range(1, cols + 1):
            elem.append(operation(row, col))
        matrix.append(elem)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=' ')
        print()