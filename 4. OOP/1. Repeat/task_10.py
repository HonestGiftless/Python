# is_decimal

import re

def is_decimal(string: str) -> bool:
    regex = r'(^-?\d+\.?\d*)$|(^-?\.?\d+$)'
    return bool(re.fullmatch(regex, string))