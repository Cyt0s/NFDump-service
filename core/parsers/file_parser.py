from abc import ABC, abstractmethod
from core.models.file import File


class FileParser(ABC):
    @abstractmethod
    def parse(self, file: File):
        pass