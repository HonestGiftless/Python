# Упаковка дубликатов 🌶️

data = input().split()
result = [[data[0]]]

for i in range(1, len(data)):
    if data[i] in result[-1]:
        result[-1].append(data[i])
    else:
        result.append([data[i]])

print(result)