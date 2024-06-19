# А сколько стоит курс?

from collections import Counter

products = sorted(Counter(input().split(',')).items(), key=lambda item: item[0])

max_length = len(max(products, key=lambda item: len(item[0]))[0])

for product in products:
    total = Counter(product[0])
    price = 0

    for k, v in total.items():
        if not k.isspace():
            price += ord(k) * v
    
    print(f"{product[0].ljust(max_length)}: {price} UC x {product[1]} = {price * product[1]} UC")