# Напишите программу, которая принимает через стандартный поток ввода (команда input()) три строки, а затем выводит их в
# обратной последовательности, каждую на отдельной строчке.

strings = reversed([input() for i in range(3)])

print(*strings, sep='\n')