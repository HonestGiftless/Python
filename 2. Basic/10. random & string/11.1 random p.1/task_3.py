# Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).

import random

def append_numbers(lst, frm, to):
    for i in range(frm, to + 1):
        lst.append(chr(i))

symbols = []
append_numbers(symbols, 65, 90)
append_numbers(symbols, 97, 122)

n = int(input())
password = ''

for i in range(n):
    rnd_num = random.randint(0, len(symbols))
    password += symbols[rnd_num]

print(password)