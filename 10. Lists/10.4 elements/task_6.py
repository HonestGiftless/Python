# Google search - 2 🌶️🌶️

n = int(input())
l = []

for _ in range(n):
    s = input()
    l.append(s)

k = int(input())
l2 = []

for _ in range(k):
    s2 = input()
    l2.append(s2)

for i in l:
    n = 0
    for j in l2:
        if j.lower() in i.lower():
            n += 1
    if n >= len(l2):
        print(i)