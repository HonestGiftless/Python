# Серединное число

a, b, c = int(input()), int(input()), int(input())

if a > b and b > c:
    print(b)
elif a > b and b < c and a > c:
    print(c)
elif b > a and a > c:
    print(a)
elif b > a and a < c and b > c:
    print(c)
elif c > a and a > b:
    print(a)
elif c > a and a < b and c > b:
    print(b)