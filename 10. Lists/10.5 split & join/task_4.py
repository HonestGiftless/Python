# Диаграмма

s = input().split()
l = []

for i in s:
    i = int(i)
    l.append(i)

for i in range(len(l)):
    print('+' * l[i])