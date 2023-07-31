from .value_object import ValueObject
from  dataclasses import dataclass
from email.utils import parseaddr
import re

@dataclass(frozen=True)
class EmailValueObject(ValueObject):
    value:str
    
    def __post_init__(self):
        real_name, email_address = parseaddr(self.value)

        if not real_name and not email_address:
            raise ValueError("Incorrect email address!")

        regex_result = re.search(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
            email_address,
        )
        if not regex_result:
            raise ValueError("Incorrect email address!")