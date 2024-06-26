# dict_travel() 🌶️🌶️

def dict_travel(nested_dicts, string=""):
    nested_dicts = dict(sorted(nested_dicts.items(), key=lambda item: item[0]))

    for k, v in nested_dicts.items():
        if not type(v) == dict:
            print(f"{string}{k}: {v}")
        else:
            dict_travel(v, string + f"{k}.")