# Next Prime 🌶️🌶️

def is_prime(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False

def get_next_prime(num):
    x = num + 1
    while is_prime(x) == False:
        x += 1
    return x

n = int(input())

print(get_next_prime(n))