from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class UseCase(ABC):
    @abstractmethod
    def execute(self,model:ModelEntity, basepath: str,):
        pass

    @abstractmethod
    def get(self,model:ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def create(self,model:ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def update(self,model:ModelEntity, nombre:str)->str:
        pass

    @abstractmethod
    def delete(self,model:ModelEntity, nombre:str)->str:
        pass