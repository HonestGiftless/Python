# is_greater()

def is_greater(lists, number):
    return any([True if sum(i) > number else False for i in lists])