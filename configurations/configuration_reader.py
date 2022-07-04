from abc import ABC, abstractmethod


class ConfigurationReader(ABC):
    @abstractmethod
    def read_configuration(self):
        pass
