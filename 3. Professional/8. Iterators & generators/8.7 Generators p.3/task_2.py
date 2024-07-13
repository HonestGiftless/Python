# parse_ranges()

def parse_ranges(ranges):
    values = (i.strip() for i in ranges.split(','))
    diapasons = (i.split('-') for i in values)
    current_ranges = ((int(i), int(j) + 1) for i, j in diapasons)
    result = (x for y in current_ranges for x in range(y[0], y[1]))

    return result