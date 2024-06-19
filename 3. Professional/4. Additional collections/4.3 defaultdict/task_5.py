# flip_dict()

from collections import defaultdict

def flip_dict(dict_of_lists):
    items = defaultdict(list)
    keys, values = set(), set()

    for k, v in dict_of_lists.items():
        for i in v:
            items[i] += [k]

    return items