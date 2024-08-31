# Queue 🌶️
class Queue:
    def __init__(self, *args) -> None:
        self.args = list(args)

    def add(self, *args):
        self.args += args

    def pop(self):
        if len(self.args) > 0:
            item = self.args.pop(0)
            if item:
                return item

    def __str__(self) -> str:
        return f"{' -> '.join(map(str, self.args))}"

    def __eq__(self, value) -> bool:
        if isinstance(value, Queue):
            return len(self.args) == len(value.args) and all([True if self.args[i] == value.args[i] else False for i in range(len(self.args))])
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, Queue):
            items = self.args + value.args
            return Queue(*items)
        return NotImplemented
    
    def __iadd__(self, value):
        if isinstance(value, Queue):
            self.args += value.args
            return self
        return NotImplemented
    
    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.args):
                return Queue()
            return Queue(*self.args[n:])
        return NotImplemented