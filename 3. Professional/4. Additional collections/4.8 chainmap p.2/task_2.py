# deep_update()

from collections import ChainMap

def deep_update(chainmap, key, value):
    has_key = any([True if key in i.keys() else False for i in chainmap.maps])

    if has_key:
        for i in chainmap.maps:
            if key in i.keys():
                i[key] = value
    else:
        chainmap.maps[0][key] = value

    return None