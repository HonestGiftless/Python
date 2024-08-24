# IPAddress

from functools import singledispatchmethod

class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress) -> None:
        raise TypeError("Неверный формат")

    @__init__.register(str)
    def _from_str(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_collections(self, ipaddress):
        self.ipaddress = ".".join([str(i) for i in ipaddress])

    def __str__(self) -> str:
        return self.ipaddress
    
    def __repr__(self) -> str:
        return f"IPAddress('{self.ipaddress}')"