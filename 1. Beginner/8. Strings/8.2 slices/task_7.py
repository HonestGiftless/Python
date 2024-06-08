# Делаем срезы 2

text = input()

third_s = text[2]
not_last = text[-2]
five = text[0:5]
without_last = text[0:-2]
even =  text[::2]
odd = text[1::2]
reverse = text[::-1]
xd = text[-1::-2]

print(third_s, not_last, five, without_last, even, odd, reverse, xd, sep='\n')