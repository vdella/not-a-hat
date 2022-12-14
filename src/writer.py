from __init__ import output_dir


def write(content: str, filename='generated.txt'):
    with open(output_dir / filename, 'w+') as f:
        f.write(content)


def print_separator() -> None:
    print("\n===========================\n")
