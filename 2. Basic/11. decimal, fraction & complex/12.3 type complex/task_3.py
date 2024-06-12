# Сопряженные числа

n = int(input())
f_num = complex(input())
s_num = complex(input())

result = (f_num**n) + (s_num**n) + (f_num**n).conjugate() + (s_num**(n+1)).conjugate()

print(result)