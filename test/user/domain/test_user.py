from src.user.domain.user import User
from  src.user.domain.email_value_object import EmailValueObject
from src.user.domain.uuid_value_object import UuidValueObject
import uuid
import pytest

def test_user_right():
    _uuid=uuid.uuid4()
    uuid_value_object = UuidValueObject(str(_uuid))
    email = "email@test.com"
    email_value_object = EmailValueObject(email)
    
    user = User(uuid_value_object,email_value_object)
    
    assert(str(_uuid) == user.uuid.value and email == user.email.value)
    