# Кремниевая долина 🌶️🌶️

virus = 'anton'

for i in range(1, int(input()) + 1):
    s, res = input(),  ''
    for j in virus:
        if j in s:
            res += j
            s = s[s.find(j):]
        
    if res == 'anton':
        print(i, end=' ')
        continue