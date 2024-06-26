# range_sum()

def range_sum(numbers, start, end):
    if end == start:
        return numbers[end]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)