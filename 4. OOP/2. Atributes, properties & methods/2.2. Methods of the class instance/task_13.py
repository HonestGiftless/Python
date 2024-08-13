# Класс Postman

class Postman:
    def __init__(self) -> None:
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        return list({}.fromkeys([h[1] for h in self.delivery_data if h[0] == street]).keys())
    
    def get_flats_for_house(self, street, house):
        return list({}.fromkeys([h[2] for h in self.delivery_data if h[0] == street and h[1] == house]).keys())