# The first letters
import re

text = input()
regex = r'\b(\w)(\w)(\w*)'

print(re.sub(regex, r'\2\1\3', text))