from file_orchestrator import FileOrchestrator
from normalizers.normalizer import Normalizer
from parsers.file_parser import FileParser
from models.file import File


class BinaryFileOrchestrator(FileOrchestrator):
    def __init__(self, normalizer: Normalizer, parser: FileParser):
        self.normalizer = normalizer
        self.parser = parser

    def orchestrate(self, file: File):
        parsed_object = self.parser.parse(file)
        normalizer = self.normalizer.normalize()
