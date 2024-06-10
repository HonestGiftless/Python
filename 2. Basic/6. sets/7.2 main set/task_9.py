# Три слова

text = input().split()

firstWord = set(text[0])
secondWord = set(text[1])
thirdWord = set(text[2])

if firstWord == secondWord == thirdWord:
    print('YES')
else:
    print('NO')