# interleave()

def interleave(*args):
    return (i for j in zip(*args) for i in j)