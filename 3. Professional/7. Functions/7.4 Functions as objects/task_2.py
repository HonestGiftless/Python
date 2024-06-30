# new print()

old_print = print

def print(*args, sep=' ', end='\n'):
    old_print(*[i.upper() if isinstance(i, str) else i for i in args], sep=sep.upper(), end=end.upper())