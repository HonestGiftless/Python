# Person

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def get_info(self):
        return self.name + ' ' + self.surname
    
    def set_info(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_info, set_info)