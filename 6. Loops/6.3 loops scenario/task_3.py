# Асимптотическое приближение

from math import log

n = int(input())

score = 0
score_sec = 0

for i in range(1, n + 1):
    score += 1 / i
    score_sec = score - log(n)
    
print(score_sec)