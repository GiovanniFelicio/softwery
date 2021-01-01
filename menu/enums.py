from enum import Enum

class EnumTypeMenu(Enum):
    
    APP = "0"
    
    @classmethod
    def choices(cls):
        return tuple((i, i .value) for i in cls)