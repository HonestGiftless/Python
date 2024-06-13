# Количество строк в файле

n = input()

with open(n, 'r', encoding='utf-8') as file:
    print(len(file.readlines()))