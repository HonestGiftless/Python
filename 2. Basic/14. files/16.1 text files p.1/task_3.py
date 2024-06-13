# Случайная строка

import random as rnd

file = open("lines.txt", 'r')

print(rnd.choice(file.readlines()))
file.close()