# Reverse order

import sys

data = list(map(str.strip, sys.stdin))

for i in data:
    print(i[::-1])