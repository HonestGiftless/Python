# Без дубликатов

n = int(input())
l = []
l2 = []

for i in range(n):
    s = input()
    l.append(s)

for i in l:
    if i not in l2:
        l2.append(i)

print(*l2, sep='\n')