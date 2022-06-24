from abc import ABC,abstractmethod


class IOCommandGenerator(ABC):
    @abstractmethod
    def generate_command(self, source, destination) -> list:
        pass