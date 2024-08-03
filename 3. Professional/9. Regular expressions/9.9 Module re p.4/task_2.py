# Logical expression
import re

print(*re.split(r'(?:\s*\|\s*)|(?:\s*&\s*)|(?:\s*(?:and)\s*)|(?:\s*(?:or)\s*)', input()), sep=', ')