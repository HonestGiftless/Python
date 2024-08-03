# Multiplying strings
import re

def func(match_obj):
    s = match_obj.group()
    item = s.split('(')
    return int(item[0]) * item[1][:-1]

txt = input()

while '(' in txt:
    txt = re.sub(r'(\d+)\((\w+)\)', func, txt)

print(txt)