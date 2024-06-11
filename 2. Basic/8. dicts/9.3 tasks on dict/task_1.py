# Словарь программиста 📘

lengthDict = int(input())
result = {}
keysAndValues = []

for _ in range(lengthDict):
        keysAndValues.append(input())

for i in keysAndValues:
        x = i.split(':')
        x[1] = x[1][1:]
        result[x[0].lower()] = x[1]
        
m = int(input())
resList = []

for _ in range(m):
        key = input().lower()
        if key in result.keys():
                resList.append(result[key])
        else:
                resList.append('Не найдено')
                
print(*resList, sep='\n')