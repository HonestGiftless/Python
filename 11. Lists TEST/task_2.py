# Сумма двух списков

s = input().split()
s2 = input().split()

l, m, e = [], [], []

for i in s:
    i = int(i)
    l.append(i)
for i in s2:
    i = int(i)
    m.append(i)

for i in range(len(l)):
    e.append(l[i] + m[i])

print(*e)