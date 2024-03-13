from enum import IntEnum

class BaseIntEnum(IntEnum):
    @classmethod
    def get_nums(cls):
        return [i.value for i in cls]

    @classmethod
    def get_names(cls):
        return [i.name for i in cls]
