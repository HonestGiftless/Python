# Класс Gun

class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        self.count += 1
        if self.count % 2 == 0:
            print("paf")
        else:
            print("pif")