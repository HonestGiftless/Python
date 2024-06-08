# Численный треугольник 1

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        x = str(i)
        z = str(j)
        if i == j:
            if i == 1:
                print(i)
            else:
                print(i * x)