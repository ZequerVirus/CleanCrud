from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class RepositoryImpl(ABC):
    nombre: str

    @abstractmethod
    def execute(self,):
        pass

    @abstractmethod
    def get_all(self,)->str:
        pass

    @abstractmethod
    def get_by_id(self,)->str:
        pass

    @abstractmethod
    def save(self,)->str:
        pass

    @abstractmethod
    def delete(self,)->str:
        pass

    @abstractmethod
    def exists_by_id(self,)->str:
        pass

    @abstractmethod
    def map(self,)->str:
        pass