# Single function

import pickle
import sys

file_name = input()

with open(file_name, "rb") as file:
    result = pickle.load(file)
    print(result(*list(map(str.strip, sys.stdin))))