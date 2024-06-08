# Взлом Братства Стали 🌶️

n = input().split('#')
n.remove('')

l = []

for i in range(int(n[0])):
    s = input()
    l.append(s)

for i in l:
    if '#' in i:
        x = i.find('#')
        i = i[0:x]
        i = i.rstrip()
        print(i)
    else:
        print(i)