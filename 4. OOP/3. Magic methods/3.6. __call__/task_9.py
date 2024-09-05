# @CachedFunction
class CachedFunction:
    def __init__(self, func) -> None:
        self.func = func
        self.cache = dict()

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]