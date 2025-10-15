from abc import ABC, abstractmethod

class Dto(ABC):
    @abstractmethod
    def execute(self,):
        pass