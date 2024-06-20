# get_value()

from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()

    for i in chainmap.maps:
        if key in i.keys():
            return i[key]
            break
            
    return None