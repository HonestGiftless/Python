# Обратный порядок 1

num = int(input())

while num != 0:
    last_d = num % 10
    print(last_d)
    num //= 10