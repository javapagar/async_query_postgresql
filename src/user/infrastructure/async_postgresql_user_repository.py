from ..domain.user_repository import UserRepository
from ..domain.user import User

class AsyncPostgresqlUserRepository(UserRepository):
    
    def __init__(self,pool):
        self.pool = pool
    
    async def create(self,user:User)->None:        
        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                try:
                    statement = f"INSERT INTO users (uuid, email) values ('{user.uuid.value}','{user.email.value}')"
                    await cursor.execute(statement)
                except Exception as e:
                    raise e