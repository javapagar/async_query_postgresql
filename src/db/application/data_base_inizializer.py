from ..domain.data_base_init_repository import DataBaseInitRepository

class DataBaseInizializer():
    
    def __init__(self, repository:DataBaseInitRepository):
        self.repository = repository
        
    def initialize(self)->None:
        self.repository.initialize()
    