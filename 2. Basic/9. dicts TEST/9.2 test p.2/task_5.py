# Слияние словарей 🌶️

def merge(dicts):
    result_dict = dict()

    for dct in dicts:
        for k, v in dct.items():
            if k not in result_dict.keys():
                result_dict[k] = set([v])
            else:
                result_dict[k].add(v)

    return result_dict