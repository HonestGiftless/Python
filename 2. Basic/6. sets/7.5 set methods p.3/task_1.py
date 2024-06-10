# Одинаковые цифры

n = set(input())
n2 = set(input())

if (n.isdisjoint(n2)):
    print('NO')
else:
    print('YES')