# pairwise()

def pairwise(iterable):
    dct = dict(enumerate(iterable, start=1))

    if len(dct) > 0:
        for k, v in dct.items():
            if k == len(dct):
                yield (v, None)
            else:
                yield (dct[k], dct[k+1])