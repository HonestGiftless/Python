# Переворот строки

with open('text.txt', 'r', encoding='utf-8') as file:
    x = file.readline()
    print(x[::-1])