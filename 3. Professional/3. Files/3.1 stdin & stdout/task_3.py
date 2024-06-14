# Лемма о трёх носках

import sys

data = [int(i.strip()) for i in sys.stdin]

if len(data) % 2 == 0:
    if data[-1] % 2 == 0:
        sys.stdout.write('Дима')
    else:
        sys.stdout.write('Анри')
else:
    if data[-1] % 2 == 0:
        sys.stdout.write('Анри')
    else:
        sys.stdout.write('Дима')