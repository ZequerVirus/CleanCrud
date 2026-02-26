from abc import ABC, abstractmethod
class PaymentService(ABC):
    @abstractmethod
    def execute(self,):
        pass