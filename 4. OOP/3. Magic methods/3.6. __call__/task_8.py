# @CountCalls
class CountCalls:
    def __init__(self, func) -> None:
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)