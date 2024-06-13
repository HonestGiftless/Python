# Схожие буквы

import string

w = [input() for i in range(3)]

ru_counter = 0
en_counter = 0

for i in w:
    if i in string.ascii_lowercase or i in string.ascii_uppercase:
        en_counter += 1
    else:
        ru_counter += 1

if ru_counter == 3:
    print('ru')
elif en_counter == 3:
    print('en')
else:
    print('mix')