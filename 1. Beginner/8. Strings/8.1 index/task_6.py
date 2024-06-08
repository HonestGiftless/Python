# Цифра 1

num = input()
total = 0

for i in range(len(num)):
    digit = int(num[i])
    total += digit
    
print(total)