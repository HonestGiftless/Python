# Операции над дробями

from fractions import Fraction

num1 = input()
num2 = input()

nl1 = num1.split('/')
nl2 = num2.split('/')
num1_list = []
num2_list = []

for i in nl1:
    num1_list.append(int(i))

for i in nl2:
    num2_list.append(int(i))

print(num1, '+', num2, '=', Fraction(num1_list[0], num1_list[1]) + Fraction(num2_list[0], num2_list[1]))
print(num1, '-', num2, '=', Fraction(num1_list[0], num1_list[1]) - Fraction(num2_list[0], num2_list[1]))
print(num1, '*', num2, '=', Fraction(num1_list[0], num1_list[1]) * Fraction(num2_list[0], num2_list[1]))
print(num1, '/', num2, '=', Fraction(num1_list[0], num1_list[1]) / Fraction(num2_list[0], num2_list[1]))