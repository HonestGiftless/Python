# Конкурсный отбор

count = int(input())
lst = []
five = []

for c in range(count):
    name = input().split()
    lst.append(name)

for i in lst:
    if i[1] == '5' or i[1] == '4':
        five.append(i)

print()

for i in lst:
    for j in i:
        print(j, end=' ')
    print()

print()

for i in five:
    for j in i:
        print(j, end=' ')
    print()