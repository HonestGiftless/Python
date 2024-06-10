# Подсписки списка 🌶️🌶️

n = input().split()
o = [[]]

k = 1

while k != len(n) + 1:
    for j in range(len(n)):
        if len(n[j:j + k]) == k:
            o.append(n[j:j + k])
    k += 1

print(o)