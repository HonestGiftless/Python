# Второе вхождение

s = input()
cnt = s.count('f')

if cnt > 1:
    x = s.find('f')
    s = s[:x] + 'a' + s[x+1:]
    new_x = s.find('f')
    print(new_x)
if cnt == 1:
    print(-1)
elif cnt < 1:
    print(-2)