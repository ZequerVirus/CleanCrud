from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class RepositoryImpl(ABC):
    @abstractmethod
    def execute(self, model: ModelEntity, basepath:str):
        pass

    @abstractmethod
    def get_all(self, model: ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def get_by_id(self, model: ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def save(self, model: ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def delete(self,model: ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def exists_by_id(self,model: ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def map(self,model: ModelEntity, nombre:str)->str:
        pass