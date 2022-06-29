from core.file_orchestrator import FileOrchestrator
from core.normalizers.normalizer import Normalizer
from core.parsers.file_parser import FileParser
from core.models.file import File
from core.serializers.file_serializer import FileSerializer
import uuid
import os


class BinaryFileOrchestrator(FileOrchestrator):
    def __init__(self, normalizer: Normalizer, parser: FileParser, serializer: FileSerializer):
        self.__normalizer = normalizer
        self.__parser = parser
        self.__serializer = serializer

    def orchestrate(self, file: File):
        self.__create_file(file)
        parsed_object = self.__parser.parse(file)
        flow_object = self.__serializer.serialize(parsed_object)
        normalized_object = self.__normalizer.normalize(flow_object)
        self.__destroy_file(file)
        return self.__serializer.deserialize(normalized_object)

    def __create_file(self, file: File):
        generated_uuid = uuid.uuid4()
        file.path = "{}{}".format("/Users/iloux/Desktop/nfdump/working/", str(generated_uuid))
        with open(file.path, "wb") as fd:
            fd.write(file.data)

    def __destroy_file(self, file: File):
        os.remove(file.path)
