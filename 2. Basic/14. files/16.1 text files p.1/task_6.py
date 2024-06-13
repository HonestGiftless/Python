# Общая стоимость

file = open("prices.txt", 'r', encoding='utf-8')
file_items = file.readlines()
items = list()
total = 0

for i in file_items:
    i.replace('\t', ' ')
    items.append(i.split())

for i in items:
    total += int(i[1]) * int(i[2])

print(total)