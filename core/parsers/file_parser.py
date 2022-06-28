from abc import ABC, abstractmethod
from core.models.file import File
from core.models.flow_object import FlowObject


class FileParser(ABC):
    @abstractmethod
    def parse(self, file: File) -> FlowObject:
        pass
