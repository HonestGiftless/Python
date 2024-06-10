# Урок математики

n = set([int(i) for i in input().split()])
n2 = set([int(i) for i in input().split()])
n3 = set([int(i) for i in input().split()])

newN = n.intersection(n2)
newN.intersection_update(n3)

if n.issuperset(newN):
    n.difference_update(newN)
if n2.issuperset(newN):
    n2.difference_update(newN)
if n3.issuperset(newN):
    n3.difference_update(newN)

result = set()
result.update(n)
result.update(n2)
result.update(n3)

result = sorted(result)

print(*result)