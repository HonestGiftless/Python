# Урок биологии

n = set([int(i) for i in input().split()])
n2 = set([int(i) for i in input().split()])
n3 = set([int(i) for i in input().split()])
evelSet = set(range(11))

evelStudents = n.union(n2)
evelStudents.update(n3)

evelSet.difference_update(evelStudents)
evelSet = sorted(evelSet)

print(*evelSet)