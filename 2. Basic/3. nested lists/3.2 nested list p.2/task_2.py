# Список по образцу 2

def printLst(lst):
    for i in lst:
        print(i, end='\n')

n = int(input())
numbers = []

for i in range(1, n + 1):
    elem = []
    for j in range(1, i + 1):
        elem.append(j)
    numbers.append(elem)
    elem = []
    
printLst(numbers)