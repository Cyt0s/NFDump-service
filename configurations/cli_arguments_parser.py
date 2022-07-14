from configurations.arguments_parser import ArgumentParser
import argparse


class CLIArgumentParser(ArgumentParser):
    def __init__(self):
        pass

    def parse(self):
        args_parser = argparse.ArgumentParser()
        args_parser.add_argument('-c', '--config', action=)
        return args_parser.parse_args()