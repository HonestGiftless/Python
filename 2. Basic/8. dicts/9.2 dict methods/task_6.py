# Самое редкое слово 🌶️

lst = [word.strip('.,!?:;-') for word in input().lower().split()]
result = {}

for i in lst:
    result[i] = result.get(i, 0) + 1
                
minimal = 10*100

for value in result.values():
    if value < minimal:
        minimal = value

rareWords = []

for k, v in result.items():
    if v == minimal:
        if v not in rareWords:
            rareWords.append(k)
        else:
            continue

rareWords = sorted(rareWords)
print(rareWords[0])