# zip_longest()

def zip_longest(*args, fill=None):
    result = list()
    maximum_length = len(max(args, key=lambda item: len(item)))

    for i in args:
        if len(i) < maximum_length:
            for j in range(maximum_length - len(i)):
                i.append(fill)

    for i in zip(*args):
        result.append(i)

    return result