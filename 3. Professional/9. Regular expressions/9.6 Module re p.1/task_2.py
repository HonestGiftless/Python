# BEEGEEK online-school
from re import search, match, fullmatch
import sys

logins = [i.strip() for i in sys.stdin]

for login in logins:
    test = fullmatch(r'_\d+[A-Za-z]*_?', login)
    print(bool(test))