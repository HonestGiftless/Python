# Подарок на новый год

with open('class_scores.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()
    list_dict = []
    for i in text:
        elem = dict()
        elem[i.split()[0]] = i.split()[1]
        list_dict.append(elem)

with open('new_scores.txt', 'w', encoding='utf-8') as file:
    for i in list_dict:
        for key, value in i.items():
            file.write(f'{key} { int(value)+5 if int(value) + 5 <= 100 else 100}\n')