from abc import ABC,abstractmethod


class IOCommandGenerator(ABC):
    @abstractmethod
    def generate_command(self, parameters: dict) -> list:
        pass