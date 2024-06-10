# Больше предыдущего

nums = [int(i) for i in input().split()]
counter = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        counter += 1

print(counter)