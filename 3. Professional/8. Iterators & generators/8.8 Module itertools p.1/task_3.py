# alnum_sequence()

import itertools as it
import string

def alnum_sequence():
    all_symbols = string.ascii_uppercase

    result = ((index + 1, char) for index, char in enumerate(all_symbols))
    rst = (elem for tpl in result for elem in tpl)

    return it.cycle(rst)