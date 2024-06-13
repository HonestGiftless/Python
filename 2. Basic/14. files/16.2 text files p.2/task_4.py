# Сумма чисел в строках

with open('numbers.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines()
    result = list()
    
    for i in lst:
        result.append([int(i) for i in i.strip('\n').split()])

    for elem in result:
        print(sum(elem))