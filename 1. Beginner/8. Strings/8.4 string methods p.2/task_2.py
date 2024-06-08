# Минутка генетики

text = input()

adenin = 0
guan = 0
citos = 0
timin = 0

for i in range(len(text)):
    if text[i] == 'А' or text[i] == 'а':
        adenin +=1
    elif text[i] == 'Г' or text[i] == 'г':
        guan += 1
    elif text[i] == 'Ц' or text[i] == 'ц':
        citos += 1
    else:
        timin += 1

print('Аденин:', adenin)
print('Гуанин:', guan)
print('Цитозин:', citos)
print('Тимин:', timin)