# Урок физики

n = set([int(i) for i in input().split()])
n2 = set([int(i) for i in input().split()])
n3 = set([int(i) for i in input().split()])

fis = n.union(n2)

n3.difference_update(fis)
n3 = sorted(n3, reverse=True)
print(*n3)