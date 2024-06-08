# Удалите нечетные индексы

n = int(input())
l = []

for i in range(n):
    num = int(input())
    l.append(num)

del l[1::2]
print(l)