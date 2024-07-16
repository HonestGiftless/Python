# roundrobin() 🌶️

import itertools as it

def roundrobin(*args):
    result = (j for i in it.zip_longest(*args, fillvalue='') for j in i if j != '')

    return result