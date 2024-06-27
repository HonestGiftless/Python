# convert()

def convert(number):
    b, o, h = bin(number), oct(number), hex(number)
    result = list()
    
    for i in [b, o, h]:
        if "-" not in i:
            result.append(i[2:].upper())
        else:
            result.append("-" + i[3:].upper())

    return tuple(result)