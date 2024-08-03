# Keywords
import re
import keyword

kwords = keyword.kwlist
text = input()

for i in kwords:
    text = re.sub(fr'(\w+)?{i}(\w+)?', r'<kw>', text, flags=re.IGNORECASE)

print(text)