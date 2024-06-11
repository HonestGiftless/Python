# Страны и города

n = int(input())
countries = []
result = {}

for _ in range(n):
    countries.append(input().split())

for i in countries:
    x = i[1:]
    result[i[0]] = x
    
cityCount = int(input())
lst = []

for i in range(cityCount):
    city = input()
    for k, v in result.items():
        if city in v:
            lst.append(k)
                
print(*lst, sep='\n')