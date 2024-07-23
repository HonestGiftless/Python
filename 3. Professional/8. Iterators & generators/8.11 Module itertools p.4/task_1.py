from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

result = groupby(sorted(sorted(persons, key=lambda item: item[0]), key=lambda item: item[2]), key=lambda item: item[2])

for i in result:
    print(f"{i[0]}:", ', '.join(str(x.name) for x in i[1]))