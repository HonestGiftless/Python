# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с
# такими сторонами.

a = int(input())
b = int(input())
c = int(input())

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print("YES")
else:
    print("NO")