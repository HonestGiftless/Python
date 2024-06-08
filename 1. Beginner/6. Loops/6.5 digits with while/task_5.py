# Вторая цифра

num = int(input())

i = 0
x = len(str(num))

while i != x - 1:
    last_d = num % 10
    i += 1
    num //= 10

print(last_d)