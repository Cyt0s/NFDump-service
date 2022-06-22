from abc import ABC,abstractmethod


class Orchestrator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def orchestrate(self):
        pass