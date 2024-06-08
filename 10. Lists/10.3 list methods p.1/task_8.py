# k-ая буква слова 🌶️🌶️

n = int(input())
l = []

for i in range(n):
    s = input()
    l.append(s)

k = int(input())

for i in l:
    if len(i) >= k:
        print(i[k - 1], end='')
    else:
        continue