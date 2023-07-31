from dataclasses import dataclass
from .uuid_value_object import UuidValueObject
from .email_value_object import EmailValueObject

@dataclass(frozen=True)
class User:
    uuid: UuidValueObject
    email: EmailValueObject