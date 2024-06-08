# Сортировка чисел

n = input().split()
l = []

for i in n:
    i = int(i)
    l.append(i)

l.sort()
print(*l)
l.sort(reverse=True)
print(*l)