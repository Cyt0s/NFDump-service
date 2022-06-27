from core.parsers.nfdump_parser import NFDumpParser
from core.parsers.command_generators.nfdump_command_generator import NFDumpCommandGenerator
from core.models.file import File
from core.parsers.serializers import json_serializer


def main():
    file_path = "/Users/iloux/Desktop/nfdump/nfcapd.202206261705"
    file_data = []
    file = File(path=file_path, data=file_data)
    command_generator = NFDumpCommandGenerator()
    serializer = json_serializer.JsonSerializer()
    parser = NFDumpParser(command_generator, serializer)
    parser.parse(file)


if __name__ == '__main__':
    main()
