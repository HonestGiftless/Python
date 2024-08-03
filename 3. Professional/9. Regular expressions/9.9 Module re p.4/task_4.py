# The sum of the numbers
import re

a, b = map(int, input().split())
digit_regex = re.compile(r'\d+')

result = digit_regex.findall(input(), pos=a, endpos=b)

if result:
    print(sum(map(int, result)))
else:
    print(0)