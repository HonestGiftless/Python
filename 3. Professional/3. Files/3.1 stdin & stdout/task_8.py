# Это точно Python?

import sys
from datetime import datetime

data = [datetime.strptime(i.strip('\n'), '%d.%m.%Y') for i in sys.stdin]
counter_up = 0
counter_down = 0

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        counter_up += 1
    elif data[i] < data[i - 1]:
        counter_down += 1

if counter_up == len(data) - 1:
    print("ASC")
elif counter_down == len(data) - 1:
    print("DESC")
else:
    print("MIX")