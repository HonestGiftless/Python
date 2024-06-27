# custom_isinstance()

def custom_isinstance(objects, typeinfo):
    return sum([1 if isinstance(i, typeinfo) else 0 for i in objects])