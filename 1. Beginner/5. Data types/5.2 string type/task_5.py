# Арифметические строки

n = input()
n2 = input()
n3 = input()

l = len(n)
l2 = len(n2)
l3 = len(n3)

mx = max(l, l2, l3)
mn = min(l, l2, l3)
av = (l + l2 + l3) - (mx + mn)

if mx - av == av - mn:
    print('YES')
else:
    print('NO')