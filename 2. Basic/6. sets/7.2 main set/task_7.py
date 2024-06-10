# Все 10 цифр

num = input() + input()
numSet = set(num)

if len(numSet) == 10: print('YES')
else: print('NO')