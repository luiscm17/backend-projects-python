import sys
from src.container.di_container import DIContainer
from src.cli.app import TaskCLI


def main():
    """
    Main entry point with dependency injection

    Returns:
        None
    """
    container = DIContainer()
    cli = TaskCLI(container)
    cli.run(sys.argv)


if __name__ == "__main__":
    main()
