# The same and different ☕️
import re

word, text = input()[:-3], input()

print(len(re.findall(fr'\b{word}ou?r\b', text, re.IGNORECASE)))