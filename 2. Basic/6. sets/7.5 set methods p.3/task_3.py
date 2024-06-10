# Урок информатики

n = set(input().split())
n2 = set(input().split())
n3 = set(input().split())

n.intersection_update(n2)

evalSet = set()

for i in n:
    if i not in n3:
        evalSet.add(int(i))

evalSet = sorted(evalSet, reverse=True)
print(*evalSet)