# is_fraction

import re

def is_fraction(string: str) -> bool:
    return bool(re.fullmatch(r'^-?\d+/0*[1-9]\d*$', string, flags=re.MULTILINE))