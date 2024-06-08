# Делители 2

def number_of_factors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    return total

n = int(input())

print(number_of_factors(n))