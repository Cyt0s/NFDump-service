from abc import ABC,abstractmethod

class BaseOrchestrator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def orchestrate(self):
        pass