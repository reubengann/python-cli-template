import argparse
import logging
import sys

from src.example import example1, example2

# Uncomment this to use project settings from environment or .env file
# from src.project_settings import settings


def main() -> int:
    # OR
    # async def main():
    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=logging.INFO,
    )

    parser = argparse.ArgumentParser()
    subp = parser.add_subparsers(
        dest="subparser_name",
        help="Your help message",
    )

    # Add commands
    cmd1_p = subp.add_parser("cmd1", help="Do command 1")
    cmd2_p = subp.add_parser("cmd2", help="Do command 2")

    # Add command line arguments to the commands
    # cmd1_p.add_argument("query")
    args = parser.parse_args()
    match args.subparser_name:
        case "cmd1":
            logging.info("Running command 1")
            example1()
            return 0
        case "cmd2":
            logging.info("Running command 2")
            example2()
            return 0
        case _:
            parser.print_help()
            return 1


if __name__ == "__main__":
    sys.exit(main())
    # OR
    # asyncio.run(main())
