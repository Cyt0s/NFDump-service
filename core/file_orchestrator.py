from abc import ABC,abstractmethod
from core.models.file import File

class FileOrchestrator(ABC):
    @abstractmethod
    def orchestrate(self, file: File):
        pass