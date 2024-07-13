# with_previous()

def with_previous(iterable):
    prev_elem = None
    for elem in iterable:
        yield elem, prev_elem
        prev_elem = elem