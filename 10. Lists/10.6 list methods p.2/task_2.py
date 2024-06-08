# Переставить min и max

n = input().split()
l = []

for i in n:
    i = int(i)
    l.append(i)

mx_i = l.index(max(l))
mn_i = l.index(min(l))

l[mx_i], l[mn_i] = l[mn_i], l[mx_i]

print(*l)