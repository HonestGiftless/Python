# Social network
import sys
import re

print(sum(bool(re.search(r'beegeek', s.strip(), re.I)) for s in sys.stdin))