# В одну строку 2

l = [i for i in input() if i in '0123456789']

print(*l, sep='')