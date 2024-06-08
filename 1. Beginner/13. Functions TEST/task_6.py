# Магические даты

def is_magic(date):
    nums = date.split('.')
    year = int(nums[2]) % 100
    if int(nums[0]) * int(nums[1]) == year:
        return True
    else:
        return False

date = input()

print(is_magic(date))