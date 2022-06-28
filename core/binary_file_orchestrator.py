from core.file_orchestrator import FileOrchestrator
from core.normalizers.normalizer import Normalizer
from core.parsers.file_parser import FileParser
from core.models.file import File


class BinaryFileOrchestrator(FileOrchestrator):
    def __init__(self, normalizer: Normalizer, parser: FileParser):
        self.__normalizer = normalizer
        self.__parser = parser

    def orchestrate(self, file: File):
        parsed_object = self.__parser.parse(file)
        normalized_object = self.__normalizer.normalize(parsed_object)
        print(normalized_object.data.head())
