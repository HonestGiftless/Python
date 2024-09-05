# SortKey 🌶️
class SortKey:
    def __init__(self, *args) -> None:
        self.args = tuple(args)
        self.result = list()

    def __call__(self, obj):
        return tuple(obj.__getattribute__(i) for i in self.args)