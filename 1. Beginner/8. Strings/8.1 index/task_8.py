# Сколько раз?

text = input()
counter_pls = 0
counter_mult = 0

for i in range(len(text)):
    if text[i] == '+':
        counter_pls += 1
    elif text[i] == '*':
        counter_mult += 1
        
print('Символ + встречается', counter_pls, 'раз')       
print('Символ * встречается', counter_mult, 'раз') 