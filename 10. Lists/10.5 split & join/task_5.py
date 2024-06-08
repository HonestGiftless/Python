# Корректный ip-адрес

s = input().split('.')
l = []
cnt = 0

for i in s:
    i = int(i)
    l.append(i)

for i in l:
    if 0 <= i <= 255:
        cnt += 1

if cnt == len(l):
    print('ДА')
else:
    print('НЕТ')