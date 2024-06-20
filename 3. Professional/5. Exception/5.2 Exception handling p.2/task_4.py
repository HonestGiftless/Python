# Only numbers

import sys

total_float = 0
total_string = 0

for i in [j.strip() for j in sys.stdin]:
    try:
        try:
            total_float += int(i)
        except ValueError:
            total_float += float(i)
    except ValueError:
        total_string += 1

print(total_float)
print(total_string)