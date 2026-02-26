from abc import ABC, abstractmethod

class Repository(ABC):
    
    @abstractmethod
    def execute(self,):
        pass