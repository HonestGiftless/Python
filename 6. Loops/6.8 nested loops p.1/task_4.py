# Звездный треугольник 🌶️🌶️

n = int(input())

average = n // 2 + 1

for i in range(1, average + 1):
    if i < average:
        print(i * '*')
    else:
        for j in range(average, 0, -1):
            print(j * '*')