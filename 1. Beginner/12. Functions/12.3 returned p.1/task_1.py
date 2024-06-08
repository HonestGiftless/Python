# Конвертер километров

def convert_to_miles(km):
    m = km * 0.6214
    return m

num = int(input())

print(convert_to_miles(num))