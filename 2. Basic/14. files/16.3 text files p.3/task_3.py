# Нумерация строк

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

with open('output.txt', 'w', encoding='utf-8') as file:
    for i in range(len(text)):
        file.write(f'{i+1}) {text[i]}')