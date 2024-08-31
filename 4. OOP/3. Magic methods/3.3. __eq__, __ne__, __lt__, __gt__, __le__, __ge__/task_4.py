# Version
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version) -> None:
        item = version.split('.')
        for i in range(3 - len(version.split('.'))):
            item.append('0')
        self.version = '.'.join(item)

    def __str__(self) -> str:
        return self.version
    
    def __repr__(self) -> str:
        return f"Version('{self.version}')"

    def __eq__(self, value) -> bool:
        if isinstance(value, Version):
            return self.version == value.version
        return NotImplemented
    
    def __lt__(self, value) -> bool:
        if isinstance(value, Version):
            curr = tuple(map(int, self.version.split('.')))
            val = tuple(map(int, value.version.split('.')))
            if curr[0] < val[0]:
                return curr[0] < val[0]
            elif curr[0] == val[0]:
                if curr[1] < val[1]:
                    return curr[1] < val[1]
                elif curr[1] == val[1]:
                    return curr[2] < val[2]
        return NotImplemented