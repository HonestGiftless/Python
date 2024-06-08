# Нижний регистр

text = input()
counter = 0

for i in range(len(text)):
    if text[i] != text[i].upper():
        counter += 1

print(counter)