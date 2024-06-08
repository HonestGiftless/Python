# Все сразу 2 🌶️

numbers = [8, 9, 10, 11]

#1
numbers.insert(1, 17)
numbers.remove(9)

#2
for i in range(4, 7):
    numbers.append(i)

#3
del numbers[0]

#4
nums = numbers.copy()
numbers += nums

#5
numbers.insert(3, 25)

print(numbers)