from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class View(ABC):
    nombre:str

    @abstractmethod
    def execute(self,):
        pass

    @abstractmethod
    def get(self,)->str:
        pass

    @abstractmethod
    def post(self,)->str:
        pass

    @abstractmethod
    def put(self,)->str:
        pass

    @abstractmethod
    def delete(self,)->str:
        pass