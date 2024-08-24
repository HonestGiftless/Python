# AnyClass

class AnyClass:
    def __init__(self, **kwargs) -> None:
        self.__dict__ = kwargs
        self.items = [f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}" for k, v in kwargs.items()]

    def __str__(self) -> str:
        return f"AnyClass: {', '.join(self.items)}"
    
    def __repr__(self) -> str:
        return f"AnyClass({', '.join(self.items)})"