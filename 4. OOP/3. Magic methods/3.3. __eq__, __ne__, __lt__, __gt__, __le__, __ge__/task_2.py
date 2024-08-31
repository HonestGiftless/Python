# Word
from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word) -> None:
        self.word = word

    def __str__(self) -> str:
        return f"{self.word.capitalize()}"

    def __repr__(self) -> str:
        return f"Word('{self.word}')"

    def __eq__(self, value) -> bool:
        if isinstance(value, Word):
            return len(self.word) == len(value.word)
        return NotImplemented
    
    def __lt__(self, value) -> bool:
        if isinstance(value, Word):
            return len(self.word) < len(value.word)
        return NotImplemented