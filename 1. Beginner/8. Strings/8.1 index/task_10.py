# Гласные и согласные

text = input()
counter1 = 0
counter2 = 0

for i in range(len(text)):
    if text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        counter1 += 1
    elif text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        counter2 += 1
        
print('Количество гласных букв равно', counter1)
print('Количество согласных букв равно', counter2)