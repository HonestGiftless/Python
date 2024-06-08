# Сумма чисел

n = input().split()
l = []
total = 0

for i in n:
    i = int(i)
    l.append(i)

for i in l:
    total += i

print(*l, sep='+', end='=')
print(total)