import subprocess
import uuid
from core.parsers.command_generators.io_command_generator import IOCommandGenerator
from core.parsers.file_parser import FileParser
from core.models.file import File


class NFDumpParser(FileParser):
    def __init__(self, nfdump_command_generator: IOCommandGenerator):
        self.__nfdump_command_generator = nfdump_command_generator

    def parse(self, file: File):
        generated_output_name = "./" + str(uuid.uuid4())
        command_word_list = self.__nfdump_command_generator.generate_command(file.path, generated_output_name)
        with open(generated_output_name, 'w') as output_file:
            process = subprocess.run(command_word_list, stdout=output_file)
