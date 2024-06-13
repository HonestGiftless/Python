# Функция spell()

def spell(*args):
    res_dict = dict()
    first_symbols = [i[0].lower() for i in args]
    first_symbols = set(first_symbols)

    for i in args:
        maximal = 0
        if len(first_symbols) > 1:
            for j in first_symbols:
                if i.lower().startswith(j) and len(i) > maximal:
                    maximal = len(i)
                    res_dict[j] = len(i)
        else:
            res_dict[args[0][0].lower()] = len(max(args, key=len))

    return res_dict