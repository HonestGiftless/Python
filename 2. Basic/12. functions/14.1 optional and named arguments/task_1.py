# Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом (в зависимости от переданных аргументов) она должна вести себя так:

def matrix(rows=1, cols=0, value=0):
    mtrx = []
    if cols == 0:
        cols = rows
        for r in range(rows):
            elem = []
            for c in range(cols):
                elem.append(value)
            mtrx.append(elem)
    else:
        for r in range(rows):
            elem = []
            for c in range(cols):
                elem.append(value)
            mtrx.append(elem)

    return mtrx