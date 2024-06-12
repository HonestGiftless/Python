# Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

import random

tickets = set()

while len(tickets) != 100:
    num = random.randint(1000000, 9999999)
    if num not in tickets:
        tickets.add(num)

print(*tickets, sep='\n')