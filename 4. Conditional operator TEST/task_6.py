# Ход слона 🌶️

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

a = x2 - x1
b = y2 - y1

if a ** 2 == b ** 2:
    print("YES")
else:
    print("NO")