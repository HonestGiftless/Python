# HTML 🌶️
import re
import sys

for line in sys.stdin:
    line = line.strip()
    link_tag = re.finditer(r'<a href=\".*\">.*</a>', line)
    for txt in link_tag:
        href = re.search(r'\".*\"', txt.group())
        text = re.search(r'>.*<', txt.group())
        if href and text:
            print(f"{href.group()[1:-1]}, {text.group()[1:-1]}")