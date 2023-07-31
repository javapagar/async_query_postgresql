from ..application.user_creator import UserCreator
from ..application.async_user_creator import AsyncUserCreator
from .postgresql_user_repository import PostgresqlUserRepository
from .async_postgresql_user_repository import AsyncPostgresqlUserRepository
from ..domain.uuid_value_object import UuidValueObject
from ..domain.email_value_object import EmailValueObject
import uuid
import aiopg
import asyncio

class UserCreateController:
    @staticmethod
    def sync_create_user_list_by_number(postgresql_connection,number_users:int=1):
        repository = PostgresqlUserRepository(postgresql_connection)
        
        creator = UserCreator(repository)
        for i in range(number_users):
            _uuid = str(uuid.uuid4()) 
            email = f"{_uuid}@test.es"
            _uuid = UuidValueObject(_uuid)
            _email = EmailValueObject(email)
            creator.create(_uuid,_email)
    
    @staticmethod
    async def async_create_user_list_by_number(dsn,event_loop,number_users:int=1):
        pool = await aiopg.create_pool(dsn)     
        tasks = []
            
        repository = AsyncPostgresqlUserRepository(pool)
        
        creator = AsyncUserCreator(repository)
        for i in range(number_users):
            _uuid = str(uuid.uuid4()) 
            email = f"{_uuid}@test.es"
            _uuid = UuidValueObject(_uuid)
            _email = EmailValueObject(email)
            tasks.append(event_loop.create_task(creator.create(_uuid,_email)))
            
        await asyncio.wait(tasks)
        pool.close()
            
        