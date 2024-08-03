# Comments 🌶️🌶️
import re
import sys

words = "".join([i for i in sys.stdin])

words = re.sub(r'^\s*\"{3}[\s\S]*?\"{3}\n?|^( +)?#.*$\n', r'', words, flags=re.MULTILINE)
words = re.sub(r'(.*)(#.*)', r'\1', words, flags=re.MULTILINE)

print(words)