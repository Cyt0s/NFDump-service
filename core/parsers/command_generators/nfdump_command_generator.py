from core.parsers.command_generators.io_command_generator import IOCommandGenerator


class NFDumpCommandGenerator(IOCommandGenerator):
    def __init__(self):
        self.__command_list_example = ["nfdump", "-r", "-o"]

    def generate_command(self, parameters: dict) -> list:
        command_list_replicate = self.__command_list_example.copy()
        command_list_replicate.insert(2, parameters.get("file_name"))
        command_list_replicate.append(parameters.get("serialize_type"))
        return command_list_replicate