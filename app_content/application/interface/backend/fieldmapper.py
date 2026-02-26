from abc import ABC, abstractmethod
from app_content.domain.entities.data_entity import FieldEntity

class FieldMapper(ABC):
    '''
    Interface for the field mapper
    '''
    @abstractmethod
    def execute(self, model_name: str, model_path: str, language_to_map: str) -> list[FieldEntity]:
        '''
        Execute the field mapper
        Args:
            model_name (str): The name of the model
            model_path (str): The path of the model
            language_to_map (str): The language to map
        Returns:
            list[FieldEntity]: The list of fields
        '''
        pass

class FieldType(ABC):
    '''
    Interface for the field type
    '''
    @abstractmethod
    def topythonfield(self,):
        
        pass

    @abstractmethod
    def toflutterfield(self,):
        pass