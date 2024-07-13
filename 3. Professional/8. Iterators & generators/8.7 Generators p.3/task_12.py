# around()

def around(iterable):
    dct = dict(enumerate(iterable, start=1))

    if len(dct) > 0:
        if len(dct) > 1:
            for k, v in dct.items():
                if k == 1:
                    yield (None, v, dct[k+1])
                else:
                    if k == len(dct):
                        yield (dct[k-1], v, None)
                    else:
                        yield (dct[k-1], v, dct[k+1])
        else:
            for v in dct.values():
                yield (None, v, None)