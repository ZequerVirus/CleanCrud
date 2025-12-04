from abc import ABC, abstractmethod
class APIGateway(ABC):
    @abstractmethod
    def execute(self,):
        pass