# Необычные страны

with open('population.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines()
    strips_lst = list()
    result = list()

    for i in lst:
        i = i.strip('\n')
        strips_lst.append(i.split('\t'))

    for i in strips_lst:
        if i[0][0] == 'G' and int(i[1]) >= 500_000:
            result.append(i)

    for i in result:
        print(i[0])