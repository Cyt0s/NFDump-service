from bootstrapper import Bootstrapper

def main():
    bootstrapper = Bootstrapper()
    runner = bootstrapper.bootstrap()
    runner.start()

if __name__ == '__main__':
    main()
