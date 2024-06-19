# wins()

from collections import defaultdict

def wins(pairs):
    items = defaultdict(set)
    
    for i in pairs:
        items[i[0]].add(i[1])

    return items