# PhoneNumber

class PhoneNumber:
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number


    def __str__(self) -> str:
        if ' ' in self.phone_number:
            item = self.phone_number.split()
            return f"({item[0]}) {item[1]}-{item[2]}"
        else:
            return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"
        
    def __repr__(self) -> str:
        if ' ' in self.phone_number:
            return f"PhoneNumber('{self.phone_number.replace(' ', '')}')"
        else:
            return f"PhoneNumber('{self.phone_number}')"