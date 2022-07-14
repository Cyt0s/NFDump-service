from abc import ABC,abstractmethod


class ArgumentParser(ABC):
    @abstractmethod
    def parse(self):
        pass
