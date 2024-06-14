# calculate_it()

import time

def calculate_it(func, *args):
    start_time = time.time()
    x = func(*args)
    return (x, time.time() - start_time)