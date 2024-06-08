# Делаем срезы 1

text = input()

symbols = len(text)
multiply = text * 3
first = text[0]
first_third = text[:3]
last_third = text[-3::]
obr = text[::-1]
alls = text[1:-1]

print(symbols, multiply, first, first_third, last_third, obr, alls, sep='\n')