# Шахматная доска

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if x1 % 2 == x2 % 2 and y1 % 2 == y2 % 2:
    print("YES")
elif x1 % 2 != x2 % 2 and y1 % 2 != y2 % 2:
    print("YES")
else:
    print("NO")