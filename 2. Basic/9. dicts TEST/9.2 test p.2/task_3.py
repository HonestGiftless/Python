# Scrabble game

result = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
          2: ['D', 'G'],
          3: ['B', 'C', 'M', 'P'],
          4: ['F', 'H', 'V', 'W', 'Y'],
          5: ['K'],
          8: ['J', 'X'],
          10: ['Q', 'Z']}

text = input().upper()
total = 0

for i in text:
    for key, value in result.items():
        if i in value:
            total += key

print(total)