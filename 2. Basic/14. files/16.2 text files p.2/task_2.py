# Обратный порядок

with open('data.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines()
    x = list()
    for i in lst:
        x.append(i.strip('\n'))
    print(*x[::-1], sep='\n')