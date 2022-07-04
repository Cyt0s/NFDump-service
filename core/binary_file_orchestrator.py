from core.file_orchestrator import FileOrchestrator
from core.normalizers.normalizer import Normalizer
from core.parsers.file_parser import FileParser
from core.models.file import File
from core.serializers.file_serializer import FileSerializer
from core.io.handler import Handler


class BinaryFileOrchestrator(FileOrchestrator):
    def __init__(self, normalizer: Normalizer, parser: FileParser, serializer: FileSerializer, handler: Handler):
        self.__normalizer = normalizer
        self.__parser = parser
        self.__serializer = serializer
        self.__handler = handler


    def orchestrate(self, file: File):
        self.__handler.create(file)
        parsed_object = self.__parser.parse(file)
        flow_object = self.__serializer.serialize(parsed_object)
        normalized_object = self.__normalizer.normalize(flow_object)
        self.__handler.delete(file)
        return self.__serializer.deserialize(normalized_object)

