def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9

class Account:
    def __init__(self, login, password) -> None:
        self._login = login
        self._password = password
        self._hashed = hash_function(self._password)

    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, _):
        raise AttributeError("Изменение логина невозможно")
    
    @property
    def password(self):
        return self._hashed

    @password.setter
    def password(self, new_password):
        self._hashed = hash_function(new_password)
        self._password = self._hashed