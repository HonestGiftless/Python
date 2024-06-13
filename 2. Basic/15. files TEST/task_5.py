# Tail of a File

with open(input(), 'r', encoding='utf-8') as file:
    lines_list = file.readlines()
    print(*lines_list[-10:], sep='')