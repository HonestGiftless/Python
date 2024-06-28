# hash_as_key()

def hash_as_key(objects):
    result = dict()

    for i in objects:
        if hash(i) not in result:
            result[hash(i)] = [i]
        else:
            result[hash(i)].append(i)

    for k in result:
        if len(result[k]) == 1:
            result[k] = result[k][0]

    return result