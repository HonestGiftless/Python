# Количество слов в тексте

text = input().upper().split()

for i in range(len(text)):
    for j in text[i]:
        if j in '.,;:-?!':
            index = text[i].index(j)
            text[i] = text[i][:index] + text[i][index+1:]

print(len(set(text)))