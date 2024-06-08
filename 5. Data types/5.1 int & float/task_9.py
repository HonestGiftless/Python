# Сортировка трех 🌶️

n1 = int(input())
n2 = int(input())
n3 = int(input())

summ = n1 + n2 + n3
minimal = min(n1, n2, n3)
maximal = max(n1, n2, n3)

print(maximal)
print(summ - (minimal + maximal))
print(minimal)