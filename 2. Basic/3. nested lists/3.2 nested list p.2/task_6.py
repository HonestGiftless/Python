# Разбиение на чанки 🌶️

text = input().split()
size = int(input())

elems = []
char = []

for i in range(0, len(text), size):
    char.append(text[i:i+size])
    if char not in elems:
        elems.append(text[i:i+size])
    else:
        continue

print(elems)