# Валидный номер 🌶️🌶️

n = input()
x = n.replace('-', '')

tn = [3, 3, 4]
fl = [1, 3, 3, 4]
l = []

if x.isdigit() and '-' in n:
    n = n.split('-')
    for i in n:
        l.append(len(i))
    if len(l) == len(fl):
        if n[0] == '7' and l == fl:
            print('YES')
        else:
            print('NO')
    elif len(l) == len(tn):
        if l == tn:
            print('YES')
        else:
            print('NO')
else:
    print('NO')