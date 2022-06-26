from core.parsers.nfdump_parser import NFDumpParser
from core.parsers.command_generators.nfdump_command_generator import NFDumpCommandGenerator
from core.models.file import File


def main():
    file_path = "/Users/iloux/Desktop/nfcapd.202206252035"
    file_data = []
    file = File(path=file_path, data=file_data)
    command_generator = NFDumpCommandGenerator()
    parser = NFDumpParser(command_generator)
    parser.parse(file)


if __name__ == '__main__':
    main()