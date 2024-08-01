# Words
import re

text, subword = input(), input()
regex = fr'\b{subword}\b'

print(len(re.findall(regex, text)))