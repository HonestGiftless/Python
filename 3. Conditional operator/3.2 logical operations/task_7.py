# Ход ладьи

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if x1 == x2 and y1 != y2:
    print('YES')
elif x1 != x2 and y1 == y2:
    print('YES')
else:
    print('NO')