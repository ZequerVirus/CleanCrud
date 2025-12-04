from abc import ABC, abstractmethod
class EmailService(ABC):
    @abstractmethod
    def execute(self,):
        pass