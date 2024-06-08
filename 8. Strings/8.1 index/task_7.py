# Цифра 2

text = input()
flag = False

for i in range(len(text)):
    if text[i] == '1' or text[i] == '2' or text[i] == '3' or text[i] == '4' or text[i] == '5' or text[i] == '6' or text[i] == '7' or text[i] == '8' or text[i] == '9' or text[i] == '0':
        flag = True

if flag == True:
    print('Цифра')
else:
    print('Цифр нет')