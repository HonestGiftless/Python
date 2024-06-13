# Сумма двух-1

file = open("numbers.txt", 'r')

x = file.readlines()
counter = 0

for i in x:
    i = i.rstrip('\n')
    counter += int(i)

file.close()

print(counter)