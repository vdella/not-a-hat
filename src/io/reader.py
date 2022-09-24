from __init__ import test_code_dir


def read(file) -> str:
    """Reads a file and :returns all of its content as a single string."""
    with open(test_code_dir / file) as f:
        lines = f.read()

    return lines


if __name__ == '__main__':
    print(read('test1.c'))
