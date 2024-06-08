# Алфавит

x = list(range(97, 123))
l = []

for i in range(26):
    wrd = chr(x[i])
    l.append(wrd * (i + 1))

print(l)