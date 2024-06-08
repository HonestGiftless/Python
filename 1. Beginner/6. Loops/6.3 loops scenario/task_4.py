# Сумма чисел 2

n = int(input())

score = 0

for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        score += i
        
if score > 0 or score < 0:
    print(score)
else:
    print(0)