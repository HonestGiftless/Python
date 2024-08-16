# Pet

class Pet:
    lst = []

    def __init__(self, name) -> None:
        self.name = name
        self.__class__.lst.append(self)

    @classmethod
    def first_pet(cls):
        if cls.lst:
            return cls.lst[0]
        else:
            return None

    @classmethod
    def last_pet(cls):
        if cls.lst:
            return cls.lst[-1]
        else:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.lst)