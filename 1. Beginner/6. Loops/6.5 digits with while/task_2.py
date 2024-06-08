# Обратный порядок 2

num = int(input())

i = 0

while num != 0:
    last_d = num % 10
    print(last_d, end='')
    num //= 10