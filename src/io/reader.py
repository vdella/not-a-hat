from __init__ import resource_dir


def read(file) -> str:
    """Reads a file and :returns all of its content as a single string."""
    with open(resource_dir / file) as f:
        lines = f.read()

    return lines


if __name__ == '__main__':
    print(read('test1.c'))
