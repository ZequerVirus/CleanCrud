from abc import ABC, abstractmethod

class Entity(ABC):
    ''' Interface for the entity generator '''
    @abstractmethod
    def execute(self,):
        ''' Generate the entity for the file
        '''
        pass