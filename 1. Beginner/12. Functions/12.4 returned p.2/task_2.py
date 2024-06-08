# Is a Number Prime? 🌶️

def is_prime(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False

n = int(input())

print(is_prime(n))