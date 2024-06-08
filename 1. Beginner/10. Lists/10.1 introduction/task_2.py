# Список букв

n = int(input())
l = list(range(97, 97 + n))
l2 = []

for i in l:
    i = chr(i)
    l2.append(i)

print(l2)