# Две половинки

text = input()

if len(text) % 2 == 0:
    aver = len(text) // 2
    first_half = text[:aver]
    last_half = text[aver:]
    new_text = last_half + first_half
else:
    aver = len(text) // 2 + 1
    first_half = text[:aver]
    last_half = text[aver:]
    new_text = last_half + first_half

print(new_text)