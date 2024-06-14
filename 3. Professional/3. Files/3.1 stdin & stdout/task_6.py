# No comments

import sys

data = [i.strip('\n') for i in sys.stdin]

for i in data:
    if not i.split("#")[0].isspace():
        sys.stdout.write(i + "\n")