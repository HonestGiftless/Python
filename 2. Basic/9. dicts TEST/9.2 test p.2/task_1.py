# Минутка генетики 🧬

dnk_to_rnk = {'A': 'U',
              'C': 'G',
              'T': 'A',
              'G': 'C'}

dnk = input().upper()
result = ''

for key, value in dnk_to_rnk.items():
    for i in dnk:
        if i in dnk_to_rnk.keys():
            if len(result) != len(dnk):
                result += dnk_to_rnk[i]

print(result)