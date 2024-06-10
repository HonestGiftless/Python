# Количество совпадающих

num1 = [int(i) for i in input().split()]
num2 = [int(i) for i in input().split()]

numbers1 = set(num1)
numbers2 = set(num2)

print(len(numbers1&numbers2))