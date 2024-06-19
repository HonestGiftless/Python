# custom_sort() 🌶️

from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    if not by_values:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict, key=lambda item: ordered_dict[item]):
            ordered_dict.move_to_end(key)

    return ordered_dict