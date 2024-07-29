# Respect
import re

greetings = [r'здравствуйте', r'доброе утро', r'добрый день', r'Добрый вечер']
text = input()
has_greet = False

for i in greetings:
    test = re.match(i, text, re.I)
    if test:
        has_greet = True
        break

print(has_greet)