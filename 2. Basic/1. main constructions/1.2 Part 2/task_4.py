# Сдвиг в развитии

n = [int(i) for i in input().split()]
lst = []

lst.append(n[-1])

for i in range(len(n) - 1):
    lst.append(n[i])

print(*lst)