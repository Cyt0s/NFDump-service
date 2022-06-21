from abc import ABC,abstractmethod


class BaseApplicationRunner(ABC):

    @abstractmethod
    def start(self):
        pass
