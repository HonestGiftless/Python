with open('data.csv', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)

    print(sum(int(i[1]) for i in line_values if i[2] == 'a'))