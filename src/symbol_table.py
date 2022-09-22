from prettytable import PrettyTable
from tabulate import tabulate


def print_separator() -> None:
    print("\n===========================\n")


def print_symbol_table(tokens: list) -> None:
    print("\nPrinting symbol table:")

    symbol_table: dict = {}
    token_table = [[t.lexpos, t.lineno, t.type, t.value] for t in tokens]

    for token in token_table:
        if token[2] == 'ID':
            if token[3] in symbol_table:
                symbol_table[token[3]][2].append(token[1])
            else:
                symbol_table[token[3]] = (token[0], token[1], [])

    headers = ["Label", "Index", "Declaration (line)", "Referenced (lines)"]
    print(tabulate([(k,) + v for k, v in symbol_table.items()], headers=headers))
