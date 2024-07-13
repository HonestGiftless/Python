# nonempty_lines()

def nonempty_lines(file):
    file_data = open(file, encoding='utf-8')
    file_lines = (line for line in file_data)
    line_values = (line.rstrip() for line in file_lines if not line.isspace())
    result_values = (line if len(line) <= 25 else '...' for line in line_values)

    return result_values