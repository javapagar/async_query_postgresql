import uuid
from  src.user.domain.email_value_object import EmailValueObject
import pytest

def test_right_uuid():
    _email = "foo@email.com"
    uuid_value_object = EmailValueObject(_email)
    
    assert(_email==uuid_value_object.value)
    
def test_error_not_valid_uuid(): 
    fake_email = "foo email"
    with pytest.raises(ValueError):
      EmailValueObject(fake_email)  
    