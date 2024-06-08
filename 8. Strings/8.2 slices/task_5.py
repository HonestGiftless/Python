# Палиндром

s = input()
aver = len(s) // 2 + 1

if s == s[::-1]:
    print('YES')
else:
    print('NO')