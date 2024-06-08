# Молодежный жаргон

n = input().split()

for i in n:
    x = i[0]
    i += i[0]
    i = i[:0] + '' + i[1:]
    i += 'ки'
    print(i, end=' ')