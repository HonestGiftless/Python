# Код Морзе

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
symbols = []

for i in range(len(letters)):
    symbols.append((letters[i], morse[i]))
        
symbolsDict = dict(symbols)

text = input().upper()

for i in text:
    if i in symbolsDict.keys():
        print(symbolsDict[i], end=' ')