from __init__ import test_code_dir
import argparse


def read(file) -> str:
    """Reads a file and :returns all of its content as a single string."""
    with open(test_code_dir / file) as f:
        lines = f.read()

    return lines


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--src", dest="src", help="Source file input", type=str)
    parser.add_argument(
        "--debug", dest="debug", help="PLY debug mode", action="store_true"
    )
    parser.add_argument(
        "--print-typecheck",
        dest="print_typecheck",
        help="Print typecheck operations",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == '__main__':
    print(read('hello_world.c'))
