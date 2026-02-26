from abc import ABC, abstractmethod
from app_content.domain.entities.model_entity import ModelEntity

class Generator(ABC):
    ''' Generator interface 
    Args:
        model: The model to generate the generator
        basepath: The base path to generate the generator
    '''
    model: ModelEntity 
    basepath: str

    @abstractmethod
    def execute(self,):
        ''' Generate the generator code '''
        pass