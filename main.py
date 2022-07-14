from bootstrapper import Bootstrapper
from configurations.cli_arguments_parser import CLIArgumentParser

def main():
    args = CLIArgumentParser.parse()
    bootstrapper = Bootstrapper(args.config)
    runner = bootstrapper.bootstrap()
    runner.start()


if __name__ == '__main__':
    main()
