# Phone numbers
from re import search
import sys

numbers = [i.strip() for i in sys.stdin]

for num in numbers:
    correct_num = search(r'(?P<country>\d{1,3})(?P<separator>-| )?(?P<city>\d{1,3})\2(?P<phone>\d{4,10})', num)
    print(f"Код страны: {correct_num.group('country')}, Код города: {correct_num.group('city')}, Номер: {correct_num.group('phone')}")