# Сумма цифр

def print_digit_sum(num):
    num = str(num)
    total = 0

    for i in num:
        total += int(i)

    print(total)

n = int(input())

print_digit_sum(n)