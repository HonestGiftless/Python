# Секретное слово

text = input()
n = int(input())
lst = []
result = {}

for _ in range(n):
    x = input()
    for i in x:
        if i == ':':
            x = x[:x.index(i)] + x[x.index(i) + 1:]
            x = x.split()
            lst.append(x)

for i in lst:
    result[i[0]] = int(i[1])

resText = ''
for s in text:
    for key, value in result.items():
        if text.count(s) == value:
            resText += key

print(resText)