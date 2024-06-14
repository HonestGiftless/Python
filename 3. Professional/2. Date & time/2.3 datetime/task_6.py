# Cosmonaut's Diary

from datetime import datetime

with open('diary.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

result_dict = dict()
rst = list()
needed_dict = dict()

for i in range(len(lines)):
    if len(lines[i].split(';')) == 2:
        rst.append(lines[i])

for i in range(1, len(rst)):
    result_dict[rst[i-1]] = lines[lines.index(rst[i-1]):lines.index(rst[i])]

result_dict[rst[-1]] = lines[lines.index(rst[-1]):]

for k in result_dict.keys():
    result_dict[k] = result_dict[k][1:]

for k, v in result_dict.items():
    k = k.strip('\n')
    comma_index = k.index(';')
    string_date = k[:comma_index] + k[comma_index + 1:]
    date = datetime.strptime(string_date, '%d.%m.%Y %H:%M')
    needed_dict[date] = v

sort_dates = dict(sorted(needed_dict.items()))

for k, v in sort_dates.items():
    if k == datetime(year=2008, month=4, day=4, hour=18, minute=55):
        v[-1] += '\n'
        v.append('\n')
    print(datetime.strftime(k, '%d.%m.%Y; %H:%M'))
    print(*v, sep='', end='')