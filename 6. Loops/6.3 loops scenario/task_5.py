# Факториал

n = int(input())

multiplication = 1

if 0 < n <= 12:
    for i in range(1, n + 1):
        multiplication *= i
        
print(multiplication)