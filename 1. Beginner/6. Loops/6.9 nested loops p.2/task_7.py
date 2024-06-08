# Простые числа

def is_prime(number):
    flag = True

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = False
                break
    else:
        flag = False

    return flag

for i in range(int(input()), int(input()) + 1):
    if is_prime(i):
        print(i)