# Google search - 1

n = int(input())
l = []
l2 = []

for i in range(n):
    s = input()
    l.append(s)

search = input()

for i in l:
    x = i.upper()
    if search.upper() in x:
        l2.append(i)

print(*l2, sep='\n')