from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class Event(ABC):
    @abstractmethod
    def execute(self, model: ModelEntity, basepath: str,):
        pass