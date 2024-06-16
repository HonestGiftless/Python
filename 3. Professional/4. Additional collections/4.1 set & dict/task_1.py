# Я и сам своего рода переводчик

import string

alphabet_dict = dict()
alphabet = string.ascii_lowercase

user_alph = input()

for i in range(len(user_alph)):
    alphabet_dict[alphabet[i]] = user_alph[i]

text = input().lower()

for i in text:
    if i in alphabet_dict.keys():
        print(alphabet_dict[i], end="")
    else:
        print(i, end="")