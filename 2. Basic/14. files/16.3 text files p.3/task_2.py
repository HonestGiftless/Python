# Случайные числа

import random

with open('random.txt', 'w', encoding='utf-8') as file:
    for i in range(25):
        if i != 24:
            file.write(str(random.randint(111, 777)) + '\n')
        else:
            file.write(str(random.randint(111, 777)))