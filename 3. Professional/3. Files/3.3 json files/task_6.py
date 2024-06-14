# JSON elements

import json
import sys

data = list(map(str.strip, sys.stdin))
data = "".join(data)

json_data = json.loads(data)

for k, v in json_data.items():
    if type(v) == list:
        result = ''
        for i in v:
            result += str(i) + ', '
        result = result[:-2]
        print(f"{k}: {result}")
    else:
        print(f"{k}: {v}")