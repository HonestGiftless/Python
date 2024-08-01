# The same and different 🍕
import re

word, text = input()[:-2], input()

print(len(re.findall(fr'\b{word}[s|z]e', text, re.IGNORECASE)))