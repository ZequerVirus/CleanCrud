from abc import ABC, abstractmethod

class Module(ABC):
    @abstractmethod
    def execute(self,):
        pass