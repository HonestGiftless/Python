# Не поленимся и запишем

from collections import Counter

for product in sorted(Counter(input().split(',')).items(), key=lambda item: item[0]):
    print(f"{product[0]}: {product[1]}")