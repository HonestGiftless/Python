# Ходы коня 🐎

s=[["." for i in range(15)] for j in range(15)]
for i in [5,9]:
    for j in [6,8]:
        s[i][j] = s[j][i] = '*'
s[7][7] = 'N'
 
st = input()
x = int(st[1])
y = ord(st[0]) - ord('a') + 1
for i in range(x-1,7+x):
    for j in range(8-y,16-y):
        print(s[i][j], end= ' ')
    print()