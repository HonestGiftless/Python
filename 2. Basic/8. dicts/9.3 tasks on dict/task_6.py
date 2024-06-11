# Телефонная книга

n = int(input())
numbersList = []
result = {}

for _ in range(n):
    numbersList.append(input().lower().split())

for i in numbersList:
    if i[1] not in result.keys():
        result[i[1]] = i[0]
    else:
        for key, value in result.items():
            if key == i[1]:
                result[key] = value + ' ' + i[0]

resList = []
m = int(input())

for _ in range(m):
    x = input().lower()
    if x in result.keys():
        resList.append(result[x])
    else:
        resList.append('абонент не найден')

print(*resList, sep='\n')