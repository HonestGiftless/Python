# get_the_fastest_func()

import time

def get_the_fastest_func(func, arg):
    result = ''
    faster = 10**60
    for i in func:
        start_time = time.time()
        i(arg)
        end_time = time.time()
        if (end_time - start_time) < faster:
            result = i
            faster = end_time - start_time
    return result