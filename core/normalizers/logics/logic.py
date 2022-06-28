from abc import ABC, abstractmethod
from core.models.flow_object import FlowObject


class Logic(ABC):
    @abstractmethod
    def run(self, flow_object: FlowObject):
        pass
