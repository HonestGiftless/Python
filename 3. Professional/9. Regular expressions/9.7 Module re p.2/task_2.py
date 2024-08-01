# Subwords
import re

text, subword = input(), input()
regex = fr'\B({subword})\B'

print(len(re.findall(regex, text)))