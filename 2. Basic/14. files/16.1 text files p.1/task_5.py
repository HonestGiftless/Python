# Сумма двух-2

file = open("nums.txt", 'r')

x = file.readlines()
nums = list()

for i in x:
    i = i.strip('\n')
    i = i.strip()
    if i != '':
        nums.append(int(i))

print(sum(nums))