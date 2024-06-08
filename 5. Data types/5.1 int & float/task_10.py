# Интересное число

num = int(input())

fn = num // 100
sn = num // 10 % 10
tn = num % 10

smn = fn + sn + tn

mxn = max(fn, sn, tn)
mnn = min(fn, sn, tn)

if 100 <= num <= 999:
    if mxn - mnn == smn - (mxn + mnn):
        print('Число интересное')
    else:
        print('Число неинтересное')
else:
    print('Ошибка')