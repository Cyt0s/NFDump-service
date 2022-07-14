from configurations.configuration_reader import ConfigurationReader
import yaml


class YamlConfigurationReader(ConfigurationReader):
    def __init__(self, path):
        self.__path = path

    def read_configuration(self):
        yaml_data = {}
        with open(self.__path, "r") as config_file:
            yaml_data = yaml.parse(config_file)
        return yaml_data
