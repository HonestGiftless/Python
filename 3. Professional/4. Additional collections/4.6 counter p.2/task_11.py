# Бесплатные курсы берут свое 😭

from collections import Counter

total_books = Counter(input().split())
total_sum = 0

for i in range(int(input())):
    buyer = input().split()
    buyer = [buyer[0], int(buyer[1])]
    if total_books[buyer[0]] > 0:
        total_books[buyer[0]] -= 1
        total_sum += buyer[1]

print(total_sum)