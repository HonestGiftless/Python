# Random name and surname

import random

def strips(lst):
    res = list()
    for i in lst:
        res.append(i.strip('\n'))
    return res

pairs_dict = dict()

with open('first_names.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines()

with open('last_names.txt', 'r', encoding='utf-8') as file:
    lst2 = file.readlines()

names = random.sample(strips(lst), 3)
second_names = random.sample(strips(lst2), 3)

for i in range(3):
    print(names[i], second_names[i])