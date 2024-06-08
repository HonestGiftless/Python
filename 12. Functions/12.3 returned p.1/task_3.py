# Делители 1

def get_factors(num):
    l = []
    for i in range(1, num + 1):
        if num % i == 0:
            l.append(i)
    return l

n = int(input())

print(get_factors(n))