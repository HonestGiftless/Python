# BirthInfo 🌶️

from functools import singledispatchmethod
from datetime import date

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date) -> None:
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(tuple)
    @__init__.register(list)
    def _from_tuple(self, birth_date):
        try:
            if len(birth_date) != 3:
                raise TypeError("Аргумент переданного типа не поддерживается")
            self.birth_date = date(birth_date[0], birth_date[1], birth_date[2])
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        curr_date = date.today()
        age = curr_date.year - self.birth_date.year

        if (curr_date.month, curr_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        return age