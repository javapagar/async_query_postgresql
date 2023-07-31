from ...domain.data_base_init_repository import DataBaseInitRepository

class PostgresqlInitRepository(DataBaseInitRepository):
    
    def __init__(self,connection):
        self.connection = connection
    
    def initialize(self):
        sql = "CREATE TABLE IF NOT EXISTS users (uuid varchar(50) PRIMARY KEY,email varchar(100)) "
        
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e

