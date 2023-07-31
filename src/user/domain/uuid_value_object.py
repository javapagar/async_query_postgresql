from .value_object import ValueObject
from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class UuidValueObject(ValueObject):
    """ Class for uuid value object

    extends:
        ValueObject
    """
    value: str
    
    def __post_init__(self):
        try:
            uuid.UUID(self.value)
        except:
            raise ValueError("UUID not valid")