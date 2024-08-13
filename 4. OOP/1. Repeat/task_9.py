# is_integer

import re

def is_integer(string: str) -> bool:
    return bool(re.findall(r'\b-?\d+\d\b', string))