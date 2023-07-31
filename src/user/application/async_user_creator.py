from ..domain.user_repository import UserRepository
from ..domain.uuid_value_object import UuidValueObject
from ..domain.email_value_object import EmailValueObject
from ..domain.user import User


class AsyncUserCreator():
    def __init__(self, repository:UserRepository):
        self.repository = repository
        
    async def create(self, uuid:UuidValueObject,email:EmailValueObject)-> None:
        user = User(uuid,email)
        
        await self.repository.create(user)

