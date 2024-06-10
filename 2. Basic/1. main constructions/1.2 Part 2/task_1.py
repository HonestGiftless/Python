# Координатные четверти

n = int(input())
first, second, third, fourth = 0, 0, 0, 0

for _ in range(n):
    nums = [int(i) for i in input().split()]
    if nums[0] > 0 and nums[1] > 0:
        first += 1
    elif nums[0] < 0 and nums[1] > 0:
        second += 1
    elif nums[0] < 0 and nums[1] < 0:
        third += 1
    elif nums[0] > 0 and nums[1] < 0:
        fourth += 1

print('Первая четверть:', first)
print('Вторая четверть:', second)
print('Третья четверть:', third)
print('Четвертая четверть:', fourth)