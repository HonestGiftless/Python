# Роскомнадзор запретил букву а 🌶️🌶️

word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()