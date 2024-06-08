# Количество артиклей

n = input().split()
c = 0

for i in n:
    if i.upper() == 'a'.upper() or i.upper() == 'an'.upper() or i.upper() == 'the'.upper():
        c += 1

print('Общее количество артиклей:', c)