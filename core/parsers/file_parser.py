from abc import ABC, abstractmethod
from core.models.file import File
from core.models.parsed_object import ParsedObject


class FileParser(ABC):
    @abstractmethod
    def parse(self, file: File) -> ParsedObject:
        pass
