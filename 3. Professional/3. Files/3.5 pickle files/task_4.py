# The checksum

import pickle

filename = input()
number = int(input())

with open(filename, "rb") as file:
    data = pickle.load(file)
    
    if type(data) is dict:
        total_numbers = sum([i for i in data.keys() if type(i) is int])
    elif type(data) is list:
        lst = [i for i in data if type(i) is int]
        total_numbers = max(lst, default=0) * min(lst, default=0)

    if number == total_numbers:
        print("Контрольные суммы совпадают")
    else:
        print("Контрольные суммы не совпадают")