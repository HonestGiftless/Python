# Time
class Time:
    def __init__(self, hours, minutes) -> None:
        self.hours = (hours % 24) + (minutes // 60)
        self.minutes = minutes - 60 * (minutes // 60)
    
    def __str__(self) -> str:
        if 0 <= self.hours <= 9:
            if 0 <= self.minutes <= 9:
                return f"0{self.hours}:0{self.minutes}"
            else:
                return f"0{self.hours}:{self.minutes}"
        else:
            if 0 <= self.minutes <= 9:
                return f"{self.hours}:0{self.minutes}"
            else:
                return f"{self.hours}:{self.minutes}"
        
    def __add__(self, value):
        if isinstance(value, Time):
            hours = self.hours + value.hours
            minutes = self.minutes + value.minutes
            return Time(hours, minutes)
        return NotImplemented
    
    def __iadd__(self, value):
        if isinstance(value, Time):
            self.hours += value.hours
            self.minutes += value.minutes

            self.hours = (self.hours % 24) + (self.minutes // 60)
            self.minutes = self.minutes - 60 * (self.minutes // 60)
            return self
        return NotImplemented