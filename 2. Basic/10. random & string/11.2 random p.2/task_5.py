# Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

# Например, слова пила и липа или пост и стоп – анаграммы.

# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

import random

word = input()
anagramma = random.sample(word, len(word))

print(*anagramma, sep='')