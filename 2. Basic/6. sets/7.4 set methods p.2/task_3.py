# Числа первой строки

num1 = [int(i) for i in input().split()]
num2 = [int(i) for i in input().split()]

numbers1 = set(num1)
numbers2 = set(num2)

numbers = numbers1 - numbers2
numbers = sorted(numbers)

print(*numbers)