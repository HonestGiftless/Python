# Сумма чисел в файле

with open('nums.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines()
    new_lst = list()
    total = 0
    
    for i in lst:
        res = ''
        for j in i:
            if j not in '0123456789':
                res += ' '
            else:
                res += j
        new_lst.append(res)

    for i in new_lst:
        x = i.split()
        for j in x:
            j = int(j)
            total += j

    print(total)