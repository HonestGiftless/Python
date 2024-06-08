# Значение функции

n = int(input())
l = []
l2 = []

for i in range(n):
    x = int(input())
    l.append(x)
    fx = x ** 2 + 2 * x + 1
    l2.append(fx)

print(*l, sep='\n')
print()
print(*l2, sep='\n')