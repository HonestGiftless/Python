# Сумма делителей

n = int(input())

divider = 0

for i in range(1, n + 1):
    if n % i == 0:
        divider += i
        
print(divider)