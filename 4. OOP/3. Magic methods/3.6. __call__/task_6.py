# Filter
class Filter:
    def __init__(self, predicate) -> None:
        if predicate is None:
            self.predicate = bool
        else:
            self.predicate = predicate

    def __call__(self, iterable):
        return [i for i in iterable if self.predicate(i)]