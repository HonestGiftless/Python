# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

total = 0

for i in range(3):
    num = int(input())

    if num > 0:
        total += num

print(total)