from abc import ABC,abstractmethod


class Handler(ABC):

    @abstractmethod
    def create(self, file):
        pass

    @abstractmethod
    def delete(self, file):
        pass