# Ревью кода-6

n = int(input())
product = 1

while n != 0:
    digit = n % 10
    product *= digit
    n //= 10
    
print(product)