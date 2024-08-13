# Coordinates

import sys

numbers = [line.strip() for line in sys.stdin]

for num in numbers:
    items = num.split(',')
    num1, num2 = float(items[0][1:]), float(items[1][1:-1])
    print(-90 <= num1 <= 90 and -180 <= num2 <= 180)