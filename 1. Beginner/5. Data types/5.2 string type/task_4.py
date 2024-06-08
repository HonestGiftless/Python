# Три города 🌆

city1 = input()
city2 = input()
city3 = input()

leng1 = len(city1)
leng2 = len(city2)
leng3 = len(city3)

maxx = max(leng1, leng2, leng3)
minn = min(leng1, leng2, leng3)

if leng1 == maxx:
    if leng2 == minn:
        print(city2)
        print(city1)
    else:
        print(city3)
        print(city1)
elif leng2 == maxx:
    if leng1 == minn:
        print(city1)
        print(city2)
    else:
        print(city3)
        print(city2)
else:
    if leng1 == minn:
        print(city1)
        print(city3)
    else:
        print(city2)
        print(city3)