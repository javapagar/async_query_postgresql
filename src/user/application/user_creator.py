from ..domain.user_repository import UserRepository
from ..domain.uuid_value_object import UuidValueObject
from ..domain.email_value_object import EmailValueObject
from ..domain.user import User


class UserCreator():
    def __init__(self, repository:UserRepository):
        self.repository = repository
        
    def create(self, uuid:UuidValueObject,email:EmailValueObject)-> None:
        user = User(uuid,email)
        
        self.repository.create(user)

