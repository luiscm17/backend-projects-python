import sys
from src.cli.app import TaskCLI


def main():
    cli = TaskCLI()
    cli.run(sys.argv)


if __name__ == "__main__":
    main()
