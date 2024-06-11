# Порядковый номер

text = input().split()
result = {}
counter = []

for w in text:
    result[w] = result.get(w, 0) + 1
    counter.append(result[w])

print(*counter)