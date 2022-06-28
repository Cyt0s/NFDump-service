import subprocess
from core.parsers.command_generators.io_command_generator import IOCommandGenerator
from core.parsers.file_parser import FileParser
from core.models.file import File
from core.models.flow_object import FlowObject
from core.parsers.serializers.file_serializer import FileSerializer


class NFDumpParser(FileParser):
    def __init__(self, nfdump_command_generator: IOCommandGenerator, serializer: FileSerializer):
        self.__serializer = serializer
        self.__nfdump_command_generator = nfdump_command_generator

    def parse(self, file: File) -> FlowObject:
        command_parameters = {"file_name": file.path, "serialize_type": self.__serializer.get_type()}
        command_word_list = self.__nfdump_command_generator.generate_command(command_parameters)
        process = subprocess.Popen(command_word_list, stdout=subprocess.PIPE)
        serialized_data = self.__serializer.serialize(process.stdout.read())
        return serialized_data
