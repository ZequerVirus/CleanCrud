from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class UseCase(ABC):
    nombre:str

    @abstractmethod
    def execute(self,):
        pass

    @abstractmethod
    def get(self,)->str:
        pass

    @abstractmethod
    def create(self,)->str:
        pass

    @abstractmethod
    def update(self,)->str:
        pass

    @abstractmethod
    def delete(self,)->str:
        pass