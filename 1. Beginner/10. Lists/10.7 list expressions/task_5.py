# Списочное выражение 1

l = [i**2 for i in range(1, int(input()) + 1)]

print(*l, sep='\n')