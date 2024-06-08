# Ход ферзя

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

a = x2 - x1
b = y2 - y1

if a ** 2 == b ** 2 or a == 0 or b == 0:
    print("YES") 
else:
    print("NO")