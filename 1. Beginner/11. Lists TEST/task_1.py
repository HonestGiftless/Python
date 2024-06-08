# Список четных

n = int(input())
l = []

for i in range(2, n + 1):
    if i % 2 == 0:
        l.append(i)

print(l)