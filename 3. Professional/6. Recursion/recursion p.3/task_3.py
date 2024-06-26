# get_value()

def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]

    for v in nested_dicts.values():
        if type(v) == dict:
            result = get_value(v, key)
            if result is not None:
                return result