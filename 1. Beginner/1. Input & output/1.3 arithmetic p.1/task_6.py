# Напишите программу, которая считает стоимость трёх компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.

monitor, sys_block, keyboard, mouse = int(input()), int(input()), int(input()), int(input())

print(3 * (monitor + sys_block + keyboard + mouse))