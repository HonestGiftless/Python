# get_all_values() 🌶️

def get_all_values(nested_dicts, key):
    result = set()

    if key in nested_dicts:
        result.add(nested_dicts[key])
    
    for v in nested_dicts.values():
        if type(v) == dict:
            if get_all_values(v, key) is not None:
                result.update(get_all_values(v, key))  

    return result