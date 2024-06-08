# Merge lists 1

def merge(list1, list2):
    l = list1 + list2
    l.sort()

    return l


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))