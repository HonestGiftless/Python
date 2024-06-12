# Почтовый индекс в Латверии имеет вид: 

# LetterLetterNumber_NumberLetterLetter

# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).
# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

import random
import string

def generate_index():
    index = ''
    symbols = string.ascii_uppercase
    for i in range(7):
        if i < 3:
            if i != 2:
                index += random.choice(symbols)
            else:
                index += str(random.randint(0, 99))
        elif i == 3:
            index += '_'
        else:
            if i == 4:
                index += str(random.randint(0, 99))
            else:
                index += random.choice(symbols)
    return index