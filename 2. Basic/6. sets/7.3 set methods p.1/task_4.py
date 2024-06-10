# Встречалось ли число раньше?

myset = set()
numbersList = [int(i) for i in input().split()]

for n in numbersList:
    if n not in myset:
        print('NO')
        myset.add(n)
    else:
        print('YES')