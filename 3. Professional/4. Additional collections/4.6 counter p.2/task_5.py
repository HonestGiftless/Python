# Все еще достоин

import sys
from collections import Counter

students = [i.strip() for i in sys.stdin]
done_students = list()

for i in students:
    done_students.append(tuple([int(j) if j.isdigit() else j for j in i.split()]))

print(sorted(done_students, key=lambda item: item[1])[1][0])