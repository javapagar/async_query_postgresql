from abc import ABC,abstractmethod
from .user import User

class UserRepository(ABC):
    @abstractmethod
    def create(self,user:User)->None:
        ...