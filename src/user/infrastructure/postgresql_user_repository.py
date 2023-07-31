from ..domain.user_repository import UserRepository
from ..domain.user import User
from psycopg2 import sql

class PostgresqlUserRepository(UserRepository):
    
    def __init__(self,connection):
        self.connection = connection
    
    def create(self,user:User)->None:        
        with self.connection.cursor() as cursor:
            try:
                statement = sql.SQL("INSERT INTO users (uuid, email) values ({uuid},{email})"
                  ).format(
                      uuid = sql.Literal(user.uuid.value),
                      email =sql.Literal(user.email.value)
                  )
                  
                cursor.execute(statement)
                
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e