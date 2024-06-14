# Statistics Lesson

import sys

data = [int(i.strip()) for i in sys.stdin]

if len(data) > 0:
    sys.stdout.write("Рост самого низкого ученика: " + str(min(data)) + "\n")
    sys.stdout.write("Рост самого высокого ученика: " + str(max(data)) + "\n")
    sys.stdout.write("Средний рост: " + str(sum(data) / len(data)))
else:
    sys.stdout.write('нет учеников')