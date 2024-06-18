import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    objects = pickle.load(file)
    for obj in objects:
        for field, value in zip(Animal._fields, obj):
            print(f"{field}: {value}")
        print()