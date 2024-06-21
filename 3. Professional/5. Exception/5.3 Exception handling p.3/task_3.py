# readme.txt

filename = input()

try:
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден")