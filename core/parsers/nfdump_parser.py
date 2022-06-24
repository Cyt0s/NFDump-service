from file_parser import FileParser
from ..models.file import File
import subprocess
from core.parsers.command_generators.io_command_generator import IOCommandGenerator
import uuid


class NFDumpParser(FileParser):
    def __init__(self, nfdump_command_generator: IOCommandGenerator):
        self.__nfdump_command_generator = nfdump_command_generator

    def parse(self, file: File):
        generated_output_name = str(uuid.uuid4())
        command_word_list= self.__nfdump_command_generator.generate_command(file.path, generated_output_name)
        process = subprocess.Popen(command_word_list)
        errors = process.stderr
        print(errors)