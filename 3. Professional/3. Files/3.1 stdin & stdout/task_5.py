# Commentator

import sys

data = [i.strip() for i in sys.stdin]
counter = 0

for i in data:
    if len(i.split('#')[0]) == 0:
        counter += 1

sys.stdout.write(str(counter))