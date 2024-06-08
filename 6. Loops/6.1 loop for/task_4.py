# Звездный прямоугольник

n = int(input())

if 1 <= n <= 20:
    for _ in range(n):
        print('*' * 19)
else:
    print('Ooppss')