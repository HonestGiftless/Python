# get_all_values()

from collections import ChainMap

def get_all_values(chainmap, key):
    result = set()

    for i in chainmap.maps:
        if key in i.keys():
            result.add(i[key])

    if len(result) > 0:
        return result
    else:
        return set()