# Суммарная стоимость

with open('ledger.txt', 'r', encoding='utf-8') as file:
    total = 0
    for i in file.readlines():
        i = i.strip('$')
        total += int(i)

    print('$' + str(total))