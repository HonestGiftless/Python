# Strip
class Strip:
    def __init__(self, chars) -> None:
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)