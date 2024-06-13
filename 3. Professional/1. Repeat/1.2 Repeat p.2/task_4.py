# Более одного

nums = [int(i) for i in input().split()]
result = []

for i in nums:
    if i not in result and nums.count(i) > 1:
        result.append(i)

print(*list(sorted(result)))