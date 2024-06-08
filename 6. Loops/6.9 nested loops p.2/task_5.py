# Цифровой корень

num = input()

while len(num) >= 2:
    total = 0
    for i in num:
        total += int(i) 
    num = str(total)

print(num)