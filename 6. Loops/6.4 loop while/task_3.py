# Количество членов

text = input()

i = 0
   
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    i += 1
    text = input()
    
print(i)