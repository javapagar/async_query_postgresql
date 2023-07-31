import uuid
from src.user.domain.uuid_value_object import UuidValueObject
import pytest

def test_right_uuid():
    _uuid = uuid.uuid4()
    uuid_value_object = UuidValueObject(str(_uuid))
    
    assert(str(_uuid)==uuid_value_object.value)
    
def test_error_not_valid_uuid(): 
    fake_uuid = "foo_uuid"
    with pytest.raises(ValueError):
      UuidValueObject(str(fake_uuid))  
    