# Ревью кода-5 🌶️

n = int(input())

while n != 0:
    last_digit = n % 10
    n //= 10
    
print(last_digit)