# Negator

from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @neg.register
    @staticmethod
    def _neg(obj: int | float):
        return -obj
    
    @neg.register
    @staticmethod
    def _neg(obj: bool):
        return not obj