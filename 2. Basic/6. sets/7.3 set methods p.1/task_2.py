# Уникальные символы 2

n = int(input())
words = ''

for _ in range(n):
    words += input().upper()

counter = set(words)
print(len(counter))