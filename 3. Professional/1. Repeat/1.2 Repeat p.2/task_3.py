# Переворатор

nums = [int(i) for i in input().split()]

n = nums[0]
x = nums[1]
y = nums[2]
a = nums[3]
b = nums[4]

prior = [i for i in range(1, n + 1)]

endless = list()

if x != 1:
    result = [prior[i] for i in range(0, x-1)]
    result += list(reversed(prior[x-1:y]))
    if y != len(prior):
        result += prior[y:]

    result[a-1:b] = list(reversed(result[a-1:b]))
else:
    result = list(reversed(prior[x-1:y]))
    if y != len(prior):
        result += prior[y:]

    result[a-1:b] = list(reversed(result[a-1:b]))

print(*result)