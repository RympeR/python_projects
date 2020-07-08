from enum import Enum, IntEnum

class Light(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

print(Light['RED'])

class Priority(IntEnum):
    LOW = 1
    NORMAL = 2
    HIGH = 3

