# User

class User:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) > 0 and new_name.isalpha():
                self._name = new_name
            else:
                raise ValueError("Некорректное имя")
        else:
            raise ValueError("Некорректное имя")

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")