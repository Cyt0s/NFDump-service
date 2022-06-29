from core.file_orchestrator import FileOrchestrator
from core.normalizers.normalizer import Normalizer
from core.parsers.file_parser import FileParser
from core.models.file import File
from core.serializers.file_serializer import FileSerializer


class BinaryFileOrchestrator(FileOrchestrator):
    def __init__(self, normalizer: Normalizer, parser: FileParser, serializer: FileSerializer):
        self.__normalizer = normalizer
        self.__parser = parser
        self.__serializer = serializer

    def orchestrate(self, file: File):
        parsed_object = self.__parser.parse(file)
        flow_object = self.__serializer.serialize(parsed_object)
        normalized_object = self.__normalizer.normalize(flow_object)
        return self.__serializer.deserialize(normalized_object)
