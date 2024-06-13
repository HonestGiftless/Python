# Максимальная группа

numbers = [i for i in range(1, int(input()) + 1)]
digit_summ = {}

for i in numbers:
    total = 0
    for j in str(i):
        total += int(j)
    
    if total not in digit_summ.keys():
        digit_summ[total] = [i]
    else:
        digit_summ[total] = digit_summ[total] + [i]

print(len(max(digit_summ.values(), key=len)))