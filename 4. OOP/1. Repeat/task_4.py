# Pokemon

import sys

cards = [line.strip() for line in sys.stdin]
cards_set = set(cards)

print(len(cards) - len(cards_set))