# Знакочередующаяся сумма

n = int(input())

score = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        score += i
    else:
        score -= i
        
print(score)