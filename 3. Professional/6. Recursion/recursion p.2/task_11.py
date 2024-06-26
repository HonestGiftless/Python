# to_binary()

def to_binary(number):
    result = ""
    if number < 2:
        return str(number % 2) + result
    else:
        return to_binary(number // 2) + str(number % 2) + result