# Общие цифры

n = int(input())
listNumbers = []
mySet = set([str(i) for i in range(10)])

for _ in range(n):
    listNumbers.append(input())

for i in listNumbers:
    newSet = set(i)
    mySet.intersection_update(newSet)

mySet = sorted(mySet)
print(*mySet)