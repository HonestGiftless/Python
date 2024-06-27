# non_negative_even()

def non_negative_even(numbers):
    return all([True if i % 2 == 0 and i >= 0 else False for i in numbers])