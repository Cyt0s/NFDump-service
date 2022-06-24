from io_command_generator import IOCommandGenerator


class NFDumpCommandGenerator(IOCommandGenerator):
    def __init__(self):
        self.__command_list_example = ["nfdump", "-r", "-o", "csv", ">"]

    def generate_command(self, source: str, destination: str) -> list:
        command_list_replicate = self.__command_list_example.copy()
        command_list_replicate.insert(2, source)
        command_list_replicate.append(destination)
        return command_list_replicate
