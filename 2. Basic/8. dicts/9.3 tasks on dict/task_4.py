# Словарь синонимов

n = int(input())
result = {}
words = []

for _ in range(n):
    word = input().split()
    words.append(word)

for i in words:
    result[i[0]] = i[1]
    
neededWord = input()
for k, v in result.items():
    if k == neededWord:
        print(v)
    elif v == neededWord:
        print(k)