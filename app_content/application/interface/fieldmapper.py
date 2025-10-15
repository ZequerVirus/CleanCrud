from abc import ABC, abstractmethod
from app_content.domain.entities.data_entity import FieldEntity

class FieldMapper(ABC):
    @abstractmethod
    def execute(self, model_name: str, model_path: str) -> list[FieldEntity]:
        pass