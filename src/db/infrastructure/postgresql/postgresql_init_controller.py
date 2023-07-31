from .postgresql_init_repository import PostgresqlInitRepository
from ...application.data_base_inizializer import DataBaseInizializer

class PostgresqlInitController():
    @staticmethod
    def init(postgresql_connection):
        init_repository = PostgresqlInitRepository(postgresql_connection)
        
        inizializer = DataBaseInizializer(init_repository)
        
        inizializer.initialize()
        
        