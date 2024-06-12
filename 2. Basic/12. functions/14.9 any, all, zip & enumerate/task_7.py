# Отличники

count = int(input())
dct = dict()

for i in range(1, count + 1):
    students_count = int(input())
    result = []
    for j in range(students_count):
        g = int(input().split()[1])
        if g == 5 and g not in result:
            result.append(g)

    dct[i] = result

if all(dct.values()):
    print("YES")
else:
    print("NO")