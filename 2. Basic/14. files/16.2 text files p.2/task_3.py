# Длинные строки

with open('lines.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines()
    x, result = list(), list()

    for i in lst:
        item = i.rstrip('\n')
        x.append(item)

    x = sorted(x, key=len, reverse=True)

    for j in x:
        if len(j) == len(x[0]):
            result.append(j)

    print(*result, sep='\n')