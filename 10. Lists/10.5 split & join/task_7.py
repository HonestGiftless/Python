# Количество совпадающих пар

s = input().split()
c = 0

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            c += 1

print(c)