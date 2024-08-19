# Formatter

from functools import singledispatch

class Formatter:
    @singledispatch
    @staticmethod
    def format(obj):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @format.register
    @staticmethod
    def _format(obj: int | float):
        if isinstance(obj, int):
            result = 'Целое'
        else:
            result = 'Вещественное'
        print(f"{result} число: {obj}")

    @format.register
    @staticmethod
    def _format(obj: list | tuple):
        if isinstance(obj, list):
            result = 'списка'
        else:
            result = 'кортежа'
        print(f"Элементы {result}: {', '.join([str(i) for i in obj])}")

    @format.register
    @staticmethod
    def _format(obj: dict):
        print(f"Пары словаря: {', '.join([str((k, v)) for k, v in obj.items()])}")