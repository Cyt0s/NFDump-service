from abc import ABC,abstractmethod
from core.models.flow_object import FlowObject


class Normalizer(ABC):
    @abstractmethod
    def normalize(self, parsed_object: FlowObject):
        pass