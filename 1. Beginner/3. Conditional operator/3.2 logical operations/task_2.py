# Напишите программу, которая принимает целое число 𝑥 и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())

if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')